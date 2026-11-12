
"""Расчёт линий Неба и Земли."""

from dataclasses import dataclass

from esoterica.core import reduce_to_energy
from .calculator import PersonalSquare


@dataclass(frozen=True, slots=True)
class PersonalLines:
    """Расчётные энергии двух личных линий."""

    heaven: int
    earth: int


def calculate_personal_lines(
    square: PersonalSquare,
) -> PersonalLines:
    """Рассчитать линии по личному квадрату."""

    if not isinstance(square, PersonalSquare):
        raise TypeError("Ожидается PersonalSquare")

    heaven = reduce_to_energy(square.top + square.bottom)
    earth = reduce_to_energy(square.left + square.right)

    return PersonalLines(
        heaven=heaven,
        earth=earth,
    )
