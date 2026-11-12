
"""Расчёт тематических зон Матрицы Судьбы."""

from dataclasses import dataclass

from esoterica.core import reduce_to_energy

from .calculator import PersonalSquare
from .inner import InnerPoints


@dataclass(frozen=True, slots=True)
class WellbeingPoints:
    """Точки линии отношений и финансов."""

    balance: int
    relationship: int
    money: int


@dataclass(frozen=True, slots=True)
class ThematicZones:
    """Тематические тройки энергий Матрицы Судьбы."""

    talents: tuple[int, int, int]
    karmic_tail: tuple[int, int, int]
    material_karma: tuple[int, int, int]
    parent_child: tuple[int, int, int]
    relationships: tuple[int, int, int]
    money: tuple[int, int, int]


def calculate_wellbeing_points(
    inner: InnerPoints,
) -> WellbeingPoints:
    """Рассчитать дополнительные точки двух каналов."""

    if not isinstance(inner, InnerPoints):
        raise TypeError("Ожидается InnerPoints")

    # Внутренние точки нижней и правой осей.
    bottom = inner.bottom.near_center
    right = inner.right.near_center

    # Общая точка баланса.
    balance = reduce_to_energy(bottom + right)

    # Дополнительная точка отношений.
    relationship = reduce_to_energy(bottom + balance)

    # Дополнительная денежная точка.
    money = reduce_to_energy(right + balance)

    return WellbeingPoints(
        balance=balance,
        relationship=relationship,
        money=money,
    )


def calculate_thematic_zones(
    square: PersonalSquare,
    inner: InnerPoints,
    wellbeing: WellbeingPoints,
) -> ThematicZones:
    """Собрать тематические зоны из рассчитанных точек."""

    if not isinstance(square, PersonalSquare):
        raise TypeError("Ожидается PersonalSquare")

    if not isinstance(inner, InnerPoints):
        raise TypeError("Ожидается InnerPoints")

    if not isinstance(wellbeing, WellbeingPoints):
        raise TypeError("Ожидается WellbeingPoints")

    return ThematicZones(

        # Таланты: сверху вниз.
        talents=(
            square.top,
            inner.top.near_outer,
            inner.top.near_center,
        ),

        # Кармический хвост: от центра к нижней вершине.
        karmic_tail=(
            inner.bottom.near_center,
            inner.bottom.near_outer,
            square.bottom,
        ),

        # Материальная карма: от центра к правой вершине.
        material_karma=(
            inner.right.near_center,
            inner.right.near_outer,
            square.right,
        ),

        # Детско-родительская зона: от левой вершины к центру.
        parent_child=(
            square.left,
            inner.left.near_outer,
            inner.left.near_center,
        ),

        # Отношения.
        relationships=(
            inner.bottom.near_center,
            wellbeing.relationship,
            wellbeing.balance,
        ),

        # Финансы.
        money=(
            wellbeing.balance,
            wellbeing.money,
            inner.right.near_center,
        ),
    )
