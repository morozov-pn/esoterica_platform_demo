from datetime import date

import pytest

from esoterica.systems.destiny_matrix import (
    PersonalSquare,
    calculate_personal_square,
)


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (date(1987, 1, 23), PersonalSquare(5, 1, 7, 13, 8)),
        (date(1986, 5, 4), PersonalSquare(4, 5, 6, 15, 3)),
        (date(1984, 10, 31), PersonalSquare(4, 10, 22, 9, 9)),
    ],
)
def test_calculate_personal_square(
    birth_date: date,
    expected: PersonalSquare,
) -> None:
    assert calculate_personal_square(birth_date) == expected


def test_calculate_personal_square_rejects_text() -> None:
    with pytest.raises(TypeError):
        calculate_personal_square("23.01.1987")  # type: ignore[arg-type]

