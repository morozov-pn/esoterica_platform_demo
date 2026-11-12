from datetime import date

import pytest

from esoterica.core import parse_birth_date


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("04.05.1986", date(1986, 5, 4)),
        ("29.02.2024", date(2024, 2, 29)),
        (" 23.01.1987 ", date(1987, 1, 23)),
    ],
)
def test_parse_birth_date(source: str, expected: date) -> None:
    assert parse_birth_date(source) == expected


@pytest.mark.parametrize(
    "invalid",
    [
        "4.5.1986",
        "1986-05-04",
        "31.02.1986",
        "29.02.2023",
        "",
    ],
)
def test_parse_birth_date_rejects_invalid_text(invalid: str) -> None:
    with pytest.raises(ValueError, match="ДД.ММ.ГГГГ"):
        parse_birth_date(invalid)


@pytest.mark.parametrize("invalid", [None, 4051986, date(1986, 5, 4), True])
def test_parse_birth_date_rejects_non_strings(invalid: object) -> None:
    with pytest.raises(TypeError):
        parse_birth_date(invalid)  # type: ignore[arg-type]

