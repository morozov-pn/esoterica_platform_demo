
from datetime import date

import pytest

from esoterica.systems.destiny_matrix import (
    AncestralSquare,
    PersonalSquare,
    DestinyMatrix,
    calculate_destiny_matrix,
)


@pytest.mark.parametrize(
    ("birth_date", "personal", "ancestral"),
    [
        (
            date(1986, 5, 4),
            PersonalSquare(4, 5, 6, 15, 3),
            AncestralSquare(9, 11, 21, 19),
        ),
        (
            date(1987, 1, 23),
            PersonalSquare(5, 1, 7, 13, 8),
            AncestralSquare(6, 8, 20, 18),
        ),
    ],
)
def test_destiny_matrix(
    birth_date,
    personal,
    ancestral,
):
    result = calculate_destiny_matrix(birth_date)

    assert result == DestinyMatrix(
        personal=personal,
        ancestral=ancestral,
    )


def test_destiny_matrix_invalid_date():
    with pytest.raises(TypeError):
        calculate_destiny_matrix("04.05.1986")
