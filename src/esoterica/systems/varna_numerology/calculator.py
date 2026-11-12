
"""Нумерологический расчёт варн по методике Альбины Матрикс.

Символическая классификация, не определяющая
социальный статус или реальные способности человека.
"""

from dataclasses import dataclass
from datetime import date, time, timedelta
from enum import Enum


class Varna(str, Enum):
    """Названия четырёх варн."""

    SHUDRA = "Шудра"
    VAISHYA = "Вайшья"
    KSHATRIYA = "Кшатрий"
    BRAHMIN = "Брахман"


_DIGIT_TO_VARNA: dict[int, Varna] = {
    1: Varna.KSHATRIYA,
    2: Varna.VAISHYA,
    3: Varna.BRAHMIN,
    4: Varna.SHUDRA,
    5: Varna.VAISHYA,
    6: Varna.BRAHMIN,
    7: Varna.SHUDRA,
    8: Varna.SHUDRA,
    9: Varna.KSHATRIYA,
}


def reduce_to_digit(value: int) -> int:
    """Привести положительное целое число к 1–9."""

    if type(value) is not int:
        raise TypeError("Ожидается целое число")

    if value < 1:
        raise ValueError("Ожидается положительное число")

    while value > 9:
        value = sum(int(digit) for digit in str(value))

    return value


def get_varna(digit: int) -> Varna:
    """Определить варну по числу от 1 до 9."""

    if type(digit) is not int:
        raise TypeError("Номер должен быть целым числом")

    if not 1 <= digit <= 9:
        raise ValueError("Номер должен быть от 1 до 9")

    return _DIGIT_TO_VARNA[digit]


@dataclass(frozen=True, slots=True)
class VarnaFactor:
    """Одна составляющая процентного распределения."""

    digit: int
    varna: Varna
    percent: int


@dataclass(frozen=True, slots=True)
class VarnaProfile:
    """Полный нумерологический профиль варн."""

    day: VarnaFactor
    month: VarnaFactor
    year: VarnaFactor
    total: VarnaFactor

    expression_digit: int
    expression_varna: Varna

    # Данные для контроля поправки на время.
    birth_date: date
    calculation_date: date
    birth_time: time | None

    @property
    def adjustment_applied(self) -> bool:
        """Была ли использована предыдущая дата."""

        return self.birth_date != self.calculation_date

    @property
    def factors(self) -> tuple[VarnaFactor, ...]:
        """Четыре составляющие с весами 40/10/10/40."""

        return (
            self.day,
            self.month,
            self.year,
            self.total,
        )

    @property
    def shares(self) -> dict[Varna, int]:
        """Суммарное распределение по четырём варнам."""

        result = {varna: 0 for varna in Varna}

        for factor in self.factors:
            result[factor.varna] += factor.percent

        return result


def calculate_varna_profile(
    birth_date: date,
    birth_time: time | None = None,
) -> VarnaProfile:
    """Рассчитать варны с возможной поправкой на время.

    При рождении с 00:00 до 00:30 включительно
    используется предыдущая календарная дата.

    Если время неизвестно, поправка не применяется.
    """

    if not isinstance(birth_date, date):
        raise TypeError(
            "birth_date должно иметь тип datetime.date"
        )

    if birth_time is not None and not isinstance(
        birth_time, time
    ):
        raise TypeError(
            "birth_time должно иметь тип datetime.time "
            "или быть None"
        )

    # Сначала используем фактическую дату.
    calculation_date = birth_date

    # Проверяем, нужна ли поправка.
    if (
        birth_time is not None
        and birth_time.hour == 0
        and birth_time.minute <= 30
    ):
        if birth_date == date.min:
            raise ValueError(
                "Невозможно перейти к дате до 01.01.0001"
            )

        calculation_date = birth_date - timedelta(days=1)

    # Все числа рассчитываются по скорректированной дате.
    day = reduce_to_digit(calculation_date.day)
    month = reduce_to_digit(calculation_date.month)
    year = reduce_to_digit(calculation_date.year)

    total = reduce_to_digit(day + month + year)
    expression = reduce_to_digit(day + month)

    return VarnaProfile(
        day=VarnaFactor(
            day, get_varna(day), 40
        ),
        month=VarnaFactor(
            month, get_varna(month), 10
        ),
        year=VarnaFactor(
            year, get_varna(year), 10
        ),
        total=VarnaFactor(
            total, get_varna(total), 40
        ),
        expression_digit=expression,
        expression_varna=get_varna(expression),

        birth_date=birth_date,
        calculation_date=calculation_date,
        birth_time=birth_time,
    )
