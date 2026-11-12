
from datetime import date

import pytest

from esoterica.systems.destiny_matrix import (
    calculate_destiny_matrix,
    calculate_personal_purpose,
)


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (date(1986, 5, 4), 3),
        (date(1987, 1, 23), 8),
        (date(1969, 5, 1), 8),
        (date(1957, 5, 16), 5),
    ],
)
def test_personal_purpose(birth_date, expected):
    matrix = calculate_destiny_matrix(birth_date)

    assert matrix.personal_purpose == expected

    assert calculate_personal_purpose(
        matrix.lines
    ) == expected


def test_personal_purpose_invalid_type():
    with pytest.raises(TypeError):
        calculate_personal_purpose("04.05.1986")
