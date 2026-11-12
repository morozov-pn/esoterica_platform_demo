
from datetime import date

import pytest

from esoterica.systems.destiny_matrix import (
    PersonalLines,
    calculate_personal_lines,
    calculate_personal_square,
    calculate_destiny_matrix,
)


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (date(1969, 5, 1), PersonalLines(18, 8)),
        (date(1957, 5, 16), PersonalLines(12, 11)),
        (date(1986, 5, 4), PersonalLines(20, 10)),
        (date(1987, 1, 23), PersonalLines(14, 12)),
    ],
)
def test_personal_lines(birth_date, expected):
    square = calculate_personal_square(birth_date)

    assert calculate_personal_lines(square) == expected

    matrix = calculate_destiny_matrix(birth_date)
    assert matrix.lines == expected


def test_personal_lines_invalid_type():
    with pytest.raises(TypeError):
        calculate_personal_lines("04.05.1986")
