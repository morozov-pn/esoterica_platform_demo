"""Базовые расчёты персональной Матрицы Судьбы."""

from dataclasses import dataclass
from datetime import date

from esoterica.core import reduce_to_energy


@dataclass(frozen=True, slots=True)
class PersonalSquare:
    """Пять базовых точек личного (диагонального) квадрата."""

    left: int
    top: int
    right: int
    bottom: int
    center: int


def calculate_personal_square(birth_date: date) -> PersonalSquare:
    """Рассчитать личный квадрат по дате рождения.

    Args:
        birth_date: Проверенная календарная дата рождения.

    Returns:
        Четыре вершины личного квадрата и его центр.

    Raises:
        TypeError: Если вместо ``datetime.date`` передан другой тип.
    """

    if not isinstance(birth_date, date):
        raise TypeError("birth_date должно иметь тип datetime.date")

    left = reduce_to_energy(birth_date.day)
    top = reduce_to_energy(birth_date.month)
    right = reduce_to_energy(birth_date.year)
    bottom = reduce_to_energy(left + top + right)
    center = reduce_to_energy(left + top + right + bottom)

    return PersonalSquare(
        left=left,
        top=top,
        right=right,
        bottom=bottom,
        center=center,
    )


@dataclass(frozen=True, slots=True)
class AncestralSquare:
    """Четыре угла родового квадрата."""

    top_left: int
    top_right: int
    bottom_right: int
    bottom_left: int


def calculate_ancestral_square(
    square: PersonalSquare,
) -> AncestralSquare:
    """Рассчитать родовой квадрат из личного."""

    if not isinstance(square, PersonalSquare):
        raise TypeError("Ожидается PersonalSquare")

    return AncestralSquare(
        top_left=reduce_to_energy(square.left + square.top),
        top_right=reduce_to_energy(square.top + square.right),
        bottom_right=reduce_to_energy(square.right + square.bottom),
        bottom_left=reduce_to_energy(square.bottom + square.left),
    )
