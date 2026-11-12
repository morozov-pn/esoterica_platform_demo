
"""Расчёт линий отца и матери."""

from dataclasses import dataclass

from esoterica.core import reduce_to_energy
from .calculator import AncestralSquare


@dataclass(frozen=True, slots=True)
class AncestralLines:
    """Итоговые энергии двух родовых линий."""

    father: int
    mother: int


def calculate_ancestral_lines(
    square: AncestralSquare,
) -> AncestralLines:
    """Рассчитать линии отца и матери."""

    if not isinstance(square, AncestralSquare):
        raise TypeError("Ожидается AncestralSquare")

    father = reduce_to_energy(
        square.top_left + square.bottom_right
    )

    mother = reduce_to_energy(
        square.top_right + square.bottom_left
    )

    return AncestralLines(
        father=father,
        mother=mother,
    )
