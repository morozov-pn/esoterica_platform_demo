
"""Расчёт семи чакр по схеме Матрицы Судьбы.

Числа являются символическими значениями методики,
а не показателями медицинского состояния.
"""

from dataclasses import dataclass

from esoterica.core import reduce_to_energy

from .calculator import PersonalSquare
from .inner import InnerPoints
from .heart import HeartPoints


@dataclass(frozen=True, slots=True)
class ChakraRow:
    """Три значения одной чакры."""

    physical: int
    energy: int
    emotions: int


@dataclass(frozen=True, slots=True)
class ChakraChart:
    """Полная таблица семи чакр."""

    sahasrara: ChakraRow
    ajna: ChakraRow
    vishuddha: ChakraRow
    anahata: ChakraRow
    manipura: ChakraRow
    svadhisthana: ChakraRow
    muladhara: ChakraRow

    @property
    def rows(self) -> tuple[ChakraRow, ...]:
        """Строки от седьмой чакры к первой."""

        return (
            self.sahasrara,
            self.ajna,
            self.vishuddha,
            self.anahata,
            self.manipura,
            self.svadhisthana,
            self.muladhara,
        )


@dataclass(frozen=True, slots=True)
class ChakraTotals:
    """Обычные суммы и приведённые энергии столбцов."""

    raw_physical: int
    raw_energy: int
    raw_emotions: int

    physical: int
    energy: int
    emotions: int


def _make_row(
    physical: int,
    energy: int,
) -> ChakraRow:
    """Создать строку и рассчитать эмоции."""

    emotions = reduce_to_energy(
        physical + energy
    )

    return ChakraRow(
        physical=physical,
        energy=energy,
        emotions=emotions,
    )


def calculate_chakras(
    square: PersonalSquare,
    inner: InnerPoints,
    heart: HeartPoints,
) -> ChakraChart:
    """Рассчитать семь строк чакральной таблицы."""

    if not isinstance(square, PersonalSquare):
        raise TypeError("Ожидается PersonalSquare")

    if not isinstance(inner, InnerPoints):
        raise TypeError("Ожидается InnerPoints")

    if not isinstance(heart, HeartPoints):
        raise TypeError("Ожидается HeartPoints")

    return ChakraChart(

        # Сахасрара: А, Б.
        sahasrara=_make_row(
            square.left,
            square.top,
        ),

        # Аджна: Л, Н.
        ajna=_make_row(
            inner.left.near_outer,
            inner.top.near_outer,
        ),

        # Вишудха: К, М.
        vishuddha=_make_row(
            inner.left.near_center,
            inner.top.near_center,
        ),

        # Анахата: Ъ, Ь.
        anahata=_make_row(
            heart.hard_sign,
            heart.soft_sign,
        ),

        # Манипура: Д, Д.
        manipura=_make_row(
            square.center,
            square.center,
        ),

        # Свадхистана: О, Р.
        svadhisthana=_make_row(
            inner.right.near_center,
            inner.bottom.near_center,
        ),

        # Муладхара: В, Г.
        muladhara=_make_row(
            square.right,
            square.bottom,
        ),
    )


def calculate_chakra_totals(
    chart: ChakraChart,
) -> ChakraTotals:
    """Рассчитать суммы трёх столбцов таблицы."""

    if not isinstance(chart, ChakraChart):
        raise TypeError("Ожидается ChakraChart")

    raw_physical = sum(
        row.physical for row in chart.rows
    )

    raw_energy = sum(
        row.energy for row in chart.rows
    )

    raw_emotions = sum(
        row.emotions for row in chart.rows
    )

    return ChakraTotals(
        raw_physical=raw_physical,
        raw_energy=raw_energy,
        raw_emotions=raw_emotions,

        physical=reduce_to_energy(raw_physical),
        energy=reduce_to_energy(raw_energy),
        emotions=reduce_to_energy(raw_emotions),
    )
