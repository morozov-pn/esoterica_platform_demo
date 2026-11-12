
"""Расчёт внутренних точек личного квадрата."""

from dataclasses import dataclass

from esoterica.core import reduce_to_energy
from .calculator import PersonalSquare


@dataclass(frozen=True, slots=True)
class AxisInnerPoints:
    """Две внутренние точки одной оси."""

    near_center: int
    near_outer: int


@dataclass(frozen=True, slots=True)
class InnerPoints:
    """Восемь внутренних точек четырёх осей."""

    left: AxisInnerPoints
    top: AxisInnerPoints
    right: AxisInnerPoints
    bottom: AxisInnerPoints


def _calculate_axis(
    outer: int,
    center: int,
) -> AxisInnerPoints:
    """Рассчитать две точки между вершиной и центром."""

    near_center = reduce_to_energy(outer + center)
    near_outer = reduce_to_energy(outer + near_center)

    return AxisInnerPoints(
        near_center=near_center,
        near_outer=near_outer,
    )


def calculate_inner_points(
    square: PersonalSquare,
) -> InnerPoints:
    """Рассчитать внутренние точки личного квадрата."""

    if not isinstance(square, PersonalSquare):
        raise TypeError("Ожидается PersonalSquare")

    center = square.center

    return InnerPoints(
        left=_calculate_axis(square.left, center),
        top=_calculate_axis(square.top, center),
        right=_calculate_axis(square.right, center),
        bottom=_calculate_axis(square.bottom, center),
    )
