
"""Дополнительные точки сердечной зоны Матрицы Судьбы."""

from dataclasses import dataclass

from esoterica.core import reduce_to_energy
from .inner import InnerPoints


@dataclass(frozen=True, slots=True)
class HeartPoints:
    """Две дополнительные точки Анахаты.

    hard_sign — Ъ, левая горизонтальная ось.
    soft_sign — Ь, верхняя вертикальная ось.
    """

    hard_sign: int
    soft_sign: int


def calculate_heart_points(
    inner: InnerPoints,
    center: int,
) -> HeartPoints:
    """Рассчитать точки Ъ и Ь через личный центр Д."""

    if not isinstance(inner, InnerPoints):
        raise TypeError("Ожидается InnerPoints")

    if type(center) is not int:
        raise TypeError("Центр должен быть целым числом")

    if not 1 <= center <= 22:
        raise ValueError("Центр должен быть от 1 до 22")

    # Ъ = К + Д.
    hard_sign = reduce_to_energy(
        inner.left.near_center + center
    )

    # Ь = М + Д.
    soft_sign = reduce_to_energy(
        inner.top.near_center + center
    )

    return HeartPoints(
        hard_sign=hard_sign,
        soft_sign=soft_sign,
    )
