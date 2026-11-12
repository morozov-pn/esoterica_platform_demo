
"""Тесты внутренних точек и тематических зон."""

from datetime import date

import pytest

from esoterica.systems.destiny_matrix import (
    AxisInnerPoints,
    InnerPoints,
    WellbeingPoints,
    ThematicZones,
    PersonalSquare,
    calculate_destiny_matrix,
    calculate_inner_points,
    calculate_wellbeing_points,
    calculate_thematic_zones,
)


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (
            date(1986, 5, 4),
            InnerPoints(
                left=AxisInnerPoints(7, 11),
                top=AxisInnerPoints(8, 13),
                right=AxisInnerPoints(9, 15),
                bottom=AxisInnerPoints(18, 6),
            ),
        ),
        (
            date(1995, 5, 6),
            InnerPoints(
                left=AxisInnerPoints(13, 19),
                top=AxisInnerPoints(12, 17),
                right=AxisInnerPoints(13, 19),
                bottom=AxisInnerPoints(6, 5),
            ),
        ),
    ],
)
def test_inner_points(birth_date, expected):
    """Проверка восьми внутренних точек."""

    matrix = calculate_destiny_matrix(birth_date)

    assert matrix.inner_points == expected


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (
            date(1986, 5, 4),
            WellbeingPoints(9, 9, 18),
        ),
        (
            date(1995, 5, 6),
            WellbeingPoints(19, 7, 5),
        ),
    ],
)
def test_wellbeing_points(birth_date, expected):
    """Проверка дополнительных точек отношений и финансов."""

    matrix = calculate_destiny_matrix(birth_date)

    assert matrix.wellbeing == expected


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (
            date(1986, 5, 4),
            ThematicZones(
                talents=(5, 13, 8),
                karmic_tail=(18, 6, 15),
                material_karma=(9, 15, 6),
                parent_child=(4, 11, 7),
                relationships=(18, 9, 9),
                money=(9, 18, 9),
            ),
        ),
        (
            date(1995, 5, 6),
            ThematicZones(
                talents=(5, 17, 12),
                karmic_tail=(6, 5, 17),
                material_karma=(13, 19, 6),
                parent_child=(6, 19, 13),
                relationships=(6, 7, 19),
                money=(19, 5, 13),
            ),
        ),
    ],
)
def test_thematic_zones(birth_date, expected):
    """Проверка всех шести тематических зон."""

    matrix = calculate_destiny_matrix(birth_date)

    assert matrix.zones == expected


def test_inner_points_invalid_type():
    """Нельзя передавать строку вместо личного квадрата."""

    with pytest.raises(TypeError):
        calculate_inner_points("04.05.1986")


def test_wellbeing_invalid_type():
    """Проверка неправильного типа внутренних точек."""

    with pytest.raises(TypeError):
        calculate_wellbeing_points("invalid")


def test_thematic_zones_invalid_type():
    """Проверка неправильного типа дополнительных точек."""

    matrix = calculate_destiny_matrix(date(1986, 5, 4))

    with pytest.raises(TypeError):
        calculate_thematic_zones(
            matrix.personal,
            matrix.inner_points,
            "invalid",
        )


def test_inner_points_preserve_22():
    """Энергия 22 должна сохраняться без уменьшения."""

    square = PersonalSquare(
        left=19,
        top=2,
        right=2,
        bottom=2,
        center=3,
    )

    result = calculate_inner_points(square)

    assert result.left.near_center == 22
    assert result.left.near_outer == 5
