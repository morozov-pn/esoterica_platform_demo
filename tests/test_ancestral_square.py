
from datetime import date

import pytest

from esoterica.systems.destiny_matrix import (
    AncestralSquare,
    calculate_ancestral_square,
    calculate_personal_square,
)


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (
            date(1984, 10, 31),
            AncestralSquare(14, 5, 4, 13),
        ),
        (
            date(1986, 5, 4),
            AncestralSquare(9, 11, 21, 19),
        ),
    ],
)
def test_ancestral_square(birth_date, expected):
    personal = calculate_personal_square(birth_date)
    ancestral = calculate_ancestral_square(personal)

    assert ancestral == expected


def test_ancestral_square_rejects_invalid_type():
    with pytest.raises(TypeError):
        calculate_ancestral_square("04.05.1986")
