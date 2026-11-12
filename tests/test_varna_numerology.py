
"""Тесты нумерологического расчёта варн."""

from datetime import date

import pytest

from esoterica.systems.varna_numerology import (
    Varna,
    reduce_to_digit,
    get_varna,
    calculate_varna_profile,
)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (1, 1),
        (9, 9),
        (10, 1),
        (22, 4),
        (29, 2),
        (1986, 6),
    ],
)
def test_reduce_to_digit(value, expected):
    """Проверить приведение к одной цифре."""

    assert reduce_to_digit(value) == expected


@pytest.mark.parametrize(
    "value",
    [True, "4", 4.0, None],
)
def test_reduce_to_digit_invalid_type(value):
    """Не принимать неправильные типы данных."""

    with pytest.raises(TypeError):
        reduce_to_digit(value)


@pytest.mark.parametrize(
    "value",
    [0, -1],
)
def test_reduce_to_digit_non_positive(value):
    """Не принимать ноль и отрицательные числа."""

    with pytest.raises(ValueError):
        reduce_to_digit(value)


@pytest.mark.parametrize(
    ("digit", "expected"),
    [
        (1, Varna.KSHATRIYA),
        (2, Varna.VAISHYA),
        (3, Varna.BRAHMIN),
        (4, Varna.SHUDRA),
        (5, Varna.VAISHYA),
        (6, Varna.BRAHMIN),
        (7, Varna.SHUDRA),
        (8, Varna.SHUDRA),
        (9, Varna.KSHATRIYA),
    ],
)
def test_get_varna(digit, expected):
    """Проверить соответствие всех цифр варнам."""

    assert get_varna(digit) == expected


@pytest.mark.parametrize(
    ("birth_date", "digits", "shares", "expression"),
    [
        (
            date(1986, 5, 4),
            (4, 5, 6, 6),
            (40, 10, 0, 50),
            (9, Varna.KSHATRIYA),
        ),
        (
            # Контрольный пример из книги.
            date(1993, 2, 3),
            (3, 2, 4, 9),
            (10, 10, 40, 40),
            (5, Varna.VAISHYA),
        ),
        (
            date(1987, 1, 23),
            (5, 1, 7, 4),
            (50, 40, 10, 0),
            (6, Varna.BRAHMIN),
        ),
    ],
)
def test_varna_profile(
    birth_date,
    digits,
    shares,
    expression,
):
    """Проверить полный расчёт варн."""

    result = calculate_varna_profile(birth_date)

    assert tuple(
        factor.digit for factor in result.factors
    ) == digits

    assert tuple(
        result.shares.values()
    ) == shares

    assert (
        result.expression_digit,
        result.expression_varna,
    ) == expression


@pytest.mark.parametrize(
    "birth_date",
    [
        date(1986, 5, 4),
        date(1993, 2, 3),
        date(1987, 1, 23),
    ],
)
def test_percentages_add_up_to_100(birth_date):
    """Распределение должно суммироваться до 100%."""

    result = calculate_varna_profile(birth_date)

    assert tuple(
        factor.percent for factor in result.factors
    ) == (40, 10, 10, 40)

    assert sum(result.shares.values()) == 100


def test_invalid_birth_date():
    """Не принимать строку вместо даты."""

    with pytest.raises(TypeError):
        calculate_varna_profile("04.05.1986")
