
"""Тестирование дополнительных точек и семи чакр."""

from datetime import date

import pytest

from esoterica.systems.destiny_matrix import (
    HeartPoints,
    ChakraRow,
    ChakraChart,
    ChakraTotals,
    calculate_destiny_matrix,
    calculate_heart_points,
    calculate_chakras,
    calculate_chakra_totals,
)


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (date(1986, 5, 4), HeartPoints(10, 11)),
        (date(1987, 1, 23), HeartPoints(21, 17)),
    ],
)
def test_heart_points(birth_date, expected):
    """Проверить точки Ъ и Ь для двух дат."""

    matrix = calculate_destiny_matrix(birth_date)

    assert matrix.heart_points == expected


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (
            date(1986, 5, 4),
            ChakraChart(
                sahasrara=ChakraRow(4, 5, 9),
                ajna=ChakraRow(11, 13, 6),
                vishuddha=ChakraRow(7, 8, 15),
                anahata=ChakraRow(10, 11, 21),
                manipura=ChakraRow(3, 3, 6),
                svadhisthana=ChakraRow(9, 18, 9),
                muladhara=ChakraRow(6, 15, 21),
            ),
        ),
        (
            date(1987, 1, 23),
            ChakraChart(
                sahasrara=ChakraRow(5, 1, 6),
                ajna=ChakraRow(18, 10, 10),
                vishuddha=ChakraRow(13, 9, 22),
                anahata=ChakraRow(21, 17, 11),
                manipura=ChakraRow(8, 8, 16),
                svadhisthana=ChakraRow(15, 21, 9),
                muladhara=ChakraRow(7, 13, 20),
            ),
        ),
    ],
)
def test_chakra_chart(birth_date, expected):
    """Проверить все семь строк карты чакр."""

    matrix = calculate_destiny_matrix(birth_date)

    assert matrix.chakras == expected
    assert len(matrix.chakras.rows) == 7


@pytest.mark.parametrize(
    ("birth_date", "expected"),
    [
        (
            date(1986, 5, 4),
            ChakraTotals(
                raw_physical=50,
                raw_energy=73,
                raw_emotions=87,
                physical=5,
                energy=10,
                emotions=15,
            ),
        ),
        (
            date(1987, 1, 23),
            ChakraTotals(
                raw_physical=87,
                raw_energy=79,
                raw_emotions=94,
                physical=15,
                energy=16,
                emotions=13,
            ),
        ),
    ],
)
def test_chakra_totals(birth_date, expected):
    """Проверить суммы и итоговые энергии."""

    matrix = calculate_destiny_matrix(birth_date)

    assert matrix.chakra_totals == expected


@pytest.mark.parametrize(
    ("center", "error"),
    [
        ("3", TypeError),
        (True, TypeError),
        (0, ValueError),
        (23, ValueError),
    ],
)
def test_heart_invalid_center(center, error):
    """Проверить неправильные значения центра."""

    matrix = calculate_destiny_matrix(date(1986, 5, 4))

    with pytest.raises(error):
        calculate_heart_points(
            matrix.inner_points,
            center,
        )


def test_heart_invalid_inner():
    """Проверить тип внутренних точек."""

    with pytest.raises(TypeError):
        calculate_heart_points("invalid", 3)


@pytest.mark.parametrize(
    "field",
    ["square", "inner", "heart"],
)
def test_chakra_invalid_types(field):
    """Проверить неправильные входные объекты."""

    matrix = calculate_destiny_matrix(date(1986, 5, 4))

    values = {
        "square": matrix.personal,
        "inner": matrix.inner_points,
        "heart": matrix.heart_points,
    }

    values[field] = "invalid"

    with pytest.raises(TypeError):
        calculate_chakras(**values)


def test_totals_invalid_type():
    """Итоги должны получать ChakraChart."""

    with pytest.raises(TypeError):
        calculate_chakra_totals("invalid")


def test_energy_22_is_preserved():
    """Энергия 22 не должна сокращаться до 4."""

    matrix = calculate_destiny_matrix(date(1987, 1, 23))

    assert matrix.chakras.vishuddha.emotions == 22


def test_anahata_uses_heart_points():
    """Анахата должна использовать те же точки Ъ и Ь."""

    matrix = calculate_destiny_matrix(date(1986, 5, 4))

    assert matrix.chakras.anahata.physical == (
        matrix.heart_points.hard_sign
    )

    assert matrix.chakras.anahata.energy == (
        matrix.heart_points.soft_sign
    )
