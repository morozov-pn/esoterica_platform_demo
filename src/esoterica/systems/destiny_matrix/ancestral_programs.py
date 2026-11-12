
"""Расчёт четырёх родовых программ Матрицы Судьбы."""

from dataclasses import dataclass

from esoterica.core import reduce_to_energy
from .calculator import AncestralSquare


@dataclass(frozen=True, slots=True)
class AncestralProgram:
    """Три энергии одной родовой программы."""

    corner: int
    near_corner: int
    near_center: int

    @property
    def energies(self) -> tuple[int, int, int]:
        """Тройка от внешнего угла к центру."""

        return (
            self.corner,
            self.near_corner,
            self.near_center,
        )


@dataclass(frozen=True, slots=True)
class AncestralPrograms:
    """Четыре родовые программы."""

    father_spiritual: AncestralProgram
    mother_spiritual: AncestralProgram
    father_material: AncestralProgram
    mother_material: AncestralProgram


def _calculate_program(
    corner: int,
    center: int,
) -> AncestralProgram:
    """Рассчитать программу из угла и личного центра."""

    near_center = reduce_to_energy(corner + center)

    near_corner = reduce_to_energy(
        corner + near_center
    )

    return AncestralProgram(
        corner=corner,
        near_corner=near_corner,
        near_center=near_center,
    )


def calculate_ancestral_programs(
    square: AncestralSquare,
    center: int,
) -> AncestralPrograms:
    """Рассчитать четыре родовых канала.

    Методика: через личный центр матрицы.
    """

    if not isinstance(square, AncestralSquare):
        raise TypeError("Ожидается AncestralSquare")

    if type(center) is not int:
        raise TypeError("Центр должен быть целым числом")

    if not 1 <= center <= 22:
        raise ValueError("Центр должен быть от 1 до 22")

    return AncestralPrograms(
        father_spiritual=_calculate_program(
            square.top_left, center
        ),
        mother_spiritual=_calculate_program(
            square.top_right, center
        ),
        father_material=_calculate_program(
            square.bottom_right, center
        ),
        mother_material=_calculate_program(
            square.bottom_left, center
        ),
    )
