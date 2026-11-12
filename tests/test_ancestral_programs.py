
"""Проверка четырёх родовых программ."""

from datetime import date

import pytest

from esoterica.systems.destiny_matrix import (
    AncestralSquare,
    AncestralProgram,
    AncestralPrograms,
    calculate_ancestral_programs,
    calculate_destiny_matrix,
)


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (
            date(1986, 5, 4),
            AncestralPrograms(
                father_spiritual=AncestralProgram(9, 21, 12),
                mother_spiritual=AncestralProgram(11, 7, 14),
                father_material=AncestralProgram(21, 9, 6),
                mother_material=AncestralProgram(19, 5, 22),
            ),
        ),
        (
            date(1987, 1, 23),
            AncestralPrograms(
                father_spiritual=AncestralProgram(6, 20, 14),
                mother_spiritual=AncestralProgram(8, 6, 16),
                father_material=AncestralProgram(20, 3, 10),
                mother_material=AncestralProgram(18, 8, 8),
            ),
        ),
    ],
)
def test_ancestral_programs(birth_date, expected):
    """Проверить родовые программы двух дат."""

    matrix = calculate_destiny_matrix(birth_date)

    assert matrix.ancestral_programs == expected


@pytest.mark.parametrize(
    ("square", "center", "error"),
    [
        ("invalid", 3, TypeError),
        (AncestralSquare(9, 11, 21, 19), "3", TypeError),
        (AncestralSquare(9, 11, 21, 19), 0, ValueError),
        (AncestralSquare(9, 11, 21, 19), 23, ValueError),
    ],
)
def test_invalid_arguments(square, center, error):
    """Проверить защиту от неправильных данных."""

    with pytest.raises(error):
        calculate_ancestral_programs(square, center)


def test_order_and_energy_22():
    """Проверить порядок точек и сохранение 22."""

    matrix = calculate_destiny_matrix(date(1986, 5, 4))

    program = matrix.ancestral_programs.mother_material

    assert program.energies == (19, 5, 22)
    assert program.near_center == 22
