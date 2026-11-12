
"""Тесты поправки на время рождения при расчёте варн."""

from datetime import date, datetime, time

import pytest

from esoterica.systems.varna_numerology import (
    Varna,
    calculate_varna_profile,
)

from esoterica.systems.destiny_matrix import (
    calculate_destiny_matrix,
)


@pytest.mark.parametrize(
    ("birth_time", "expected_adjustment"),
    [
        (time(0, 0), True),
        (time(0, 29), True),
        (time(0, 30), True),
        (time(0, 30, 59), True),
        (time(0, 31), False),
        (time(12, 0), False),
        (time(23, 59), False),
    ],
)
def test_time_boundaries(birth_time, expected_adjustment):
    """Проверить границы ночного интервала."""

    profile = calculate_varna_profile(
        date(1986, 5, 4),
        birth_time,
    )

    assert profile.adjustment_applied == expected_adjustment


@pytest.mark.parametrize(
    ("birth_date", "expected_date"),
    [
        (
            date(2024, 3, 1),
            date(2024, 2, 29),
        ),
        (
            date(2025, 1, 1),
            date(2024, 12, 31),
        ),
        (
            date(2026, 5, 1),
            date(2026, 4, 30),
        ),
    ],
)
def test_previous_calendar_date(birth_date, expected_date):
    """Проверить переход месяца, года и високосный день."""

    profile = calculate_varna_profile(
        birth_date,
        time(0, 15),
    )

    assert profile.calculation_date == expected_date


def test_adjusted_varna_values():
    """Проверить полный пересчёт варн после поправки."""

    profile = calculate_varna_profile(
        date(1986, 5, 4),
        time(0, 15),
    )

    assert profile.calculation_date == date(1986, 5, 3)

    assert tuple(
        factor.digit for factor in profile.factors
    ) == (3, 5, 6, 5)

    assert profile.shares == {
        Varna.SHUDRA: 0,
        Varna.VAISHYA: 50,
        Varna.KSHATRIYA: 0,
        Varna.BRAHMIN: 50,
    }

    assert profile.expression_digit == 8
    assert profile.expression_varna == Varna.SHUDRA


def test_unknown_birth_time():
    """Не применять поправку при неизвестном времени."""

    birth_date = date(1986, 5, 4)

    without_time = calculate_varna_profile(birth_date)
    explicit_none = calculate_varna_profile(
        birth_date, None
    )

    assert without_time == explicit_none
    assert without_time.calculation_date == birth_date
    assert without_time.adjustment_applied is False


@pytest.mark.parametrize(
    "invalid_time",
    [
        "00:15",
        15,
        True,
        datetime(1986, 5, 4, 0, 15),
    ],
)
def test_invalid_birth_time(invalid_time):
    """Неправильный тип времени должен вызывать ошибку."""

    with pytest.raises(TypeError):
        calculate_varna_profile(
            date(1986, 5, 4),
            invalid_time,
        )


def test_minimum_date():
    """Не выходить за нижнюю границу календаря Python."""

    with pytest.raises(ValueError):
        calculate_varna_profile(
            date.min,
            time(0, 0),
        )


def test_destiny_matrix_is_not_adjusted():
    """Поправка варн не должна изменять Матрицу Судьбы."""

    birth_date = date(1986, 5, 4)

    matrix = calculate_destiny_matrix(birth_date)

    profile = calculate_varna_profile(
        birth_date,
        time(0, 15),
    )

    assert matrix.personal.left == 4
    assert profile.day.digit == 3
    assert profile.calculation_date == date(1986, 5, 3)
