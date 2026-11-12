"""Преобразование текстового ввода календарных дат."""

import re
from datetime import date


_BIRTH_DATE_PATTERN = re.compile(r"[0-9]{2}\.[0-9]{2}\.[0-9]{4}")
_BIRTH_DATE_ERROR = (
    "дата рождения должна иметь формат ДД.ММ.ГГГГ "
    "и быть существующей календарной датой"
)


def parse_birth_date(value: str) -> date:
    """Преобразовать строку ``ДД.ММ.ГГГГ`` в календарную дату.

    Пробелы до и после даты удаляются. Внутренний формат остаётся строгим:
    день и месяц записываются двумя цифрами, год — четырьмя.

    Args:
        value: Текстовая дата рождения.

    Returns:
        Проверенная календарная дата.

    Raises:
        TypeError: Если передана не строка.
        ValueError: Если формат неверен или такой даты не существует.
    """

    if not isinstance(value, str):
        raise TypeError("value должно быть строкой")

    normalized = value.strip()
    if _BIRTH_DATE_PATTERN.fullmatch(normalized) is None:
        raise ValueError(_BIRTH_DATE_ERROR)

    day_text, month_text, year_text = normalized.split(".")

    try:
        return date(
            year=int(year_text),
            month=int(month_text),
            day=int(day_text),
        )
    except ValueError as error:
        raise ValueError(_BIRTH_DATE_ERROR) from error

