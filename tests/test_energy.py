import pytest

from esoterica.core import reduce_to_energy


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        (1, 1),
        (22, 22),
        (23, 5),
        (29, 11),
        (48, 12),
        (1986, 6),
    ],
)
def test_reduce_to_energy(source: int, expected: int) -> None:
    assert reduce_to_energy(source) == expected


@pytest.mark.parametrize("invalid", [0, -1])
def test_reduce_to_energy_rejects_non_positive_values(invalid: int) -> None:
    with pytest.raises(ValueError):
        reduce_to_energy(invalid)


@pytest.mark.parametrize("invalid", [True, 22.0, "22", None])
def test_reduce_to_energy_rejects_non_integers(invalid: object) -> None:
    with pytest.raises(TypeError):
        reduce_to_energy(invalid)  # type: ignore[arg-type]

