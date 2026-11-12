
"""Тесты системы предназначений."""

from datetime import date

import pytest

from esoterica.systems.destiny_matrix import (
    calculate_destiny_matrix,
    calculate_ancestral_lines,
    calculate_social_purpose,
    calculate_spiritual_purpose,
    calculate_planetary_purpose,
)


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (
            date(1986, 5, 4),
            (3, 3, 3, 6, 9, 15),
        ),
        (
            date(1987, 1, 23),
            (8, 8, 8, 16, 6, 22),
        ),
        (
            date(1969, 5, 1),
            (8, 8, 8, 16, 6, 22),
        ),
        (
            date(1984, 10, 31),
            (18, 18, 9, 9, 18, 9),
        ),
    ],
)
def test_full_purpose(birth_date, expected):
    matrix = calculate_destiny_matrix(birth_date)

    actual = (
        matrix.ancestral_lines.father,
        matrix.ancestral_lines.mother,
        matrix.personal_purpose,
        matrix.social_purpose,
        matrix.spiritual_purpose,
        matrix.planetary_purpose,
    )

    assert actual == expected


def test_ancestral_lines_invalid_type():
    with pytest.raises(TypeError):
        calculate_ancestral_lines("04.05.1986")


def test_social_purpose_invalid_type():
    with pytest.raises(TypeError):
        calculate_social_purpose("04.05.1986")


@pytest.mark.parametrize(
    ("first", "second", "error"),
    [
        (True, 6, TypeError),
        (0, 6, ValueError),
        (23, 6, ValueError),
        (3, None, TypeError),
    ],
)
def test_spiritual_purpose_invalid_values(
    first, second, error
):
    with pytest.raises(error):
        calculate_spiritual_purpose(first, second)


def test_planetary_purpose_invalid_value():
    with pytest.raises(ValueError):
        calculate_planetary_purpose(16, 0)


def test_planetary_purpose_preserves_22():
    assert calculate_planetary_purpose(16, 6) == 22
