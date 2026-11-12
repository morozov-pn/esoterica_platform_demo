
"""Расчёт предназначений в Матрице Судьбы."""

from esoterica.core import reduce_to_energy

from .lines import PersonalLines
from .lineage import AncestralLines


def calculate_personal_purpose(
    lines: PersonalLines,
) -> int:
    """Рассчитать личное предназначение."""

    if not isinstance(lines, PersonalLines):
        raise TypeError("Ожидается PersonalLines")

    return reduce_to_energy(
        lines.heaven + lines.earth
    )


def _combine_energies(first: int, second: int) -> int:
    """Сложить две энергии из диапазона 1–22."""

    for value in (first, second):
        if type(value) is not int:
            raise TypeError("Энергия должна быть целым числом")

        if not 1 <= value <= 22:
            raise ValueError("Энергия должна быть от 1 до 22")

    return reduce_to_energy(first + second)


def calculate_social_purpose(
    lines: AncestralLines,
) -> int:
    """Рассчитать социальное предназначение."""

    if not isinstance(lines, AncestralLines):
        raise TypeError("Ожидается AncestralLines")

    return _combine_energies(
        lines.father,
        lines.mother,
    )


def calculate_spiritual_purpose(
    personal_purpose: int,
    social_purpose: int,
) -> int:
    """Рассчитать духовное предназначение."""

    return _combine_energies(
        personal_purpose,
        social_purpose,
    )


def calculate_planetary_purpose(
    social_purpose: int,
    spiritual_purpose: int,
) -> int:
    """Рассчитать планетарное предназначение."""

    return _combine_energies(
        social_purpose,
        spiritual_purpose,
    )
