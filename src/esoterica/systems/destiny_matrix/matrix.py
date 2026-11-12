
"""Единая модель расчёта Матрицы Судьбы."""

from dataclasses import dataclass
from datetime import date

from .calculator import (
    PersonalSquare,
    AncestralSquare,
    calculate_personal_square,
    calculate_ancestral_square,
)

from .lines import (
    PersonalLines,
    calculate_personal_lines,
)

from .lineage import (
    AncestralLines,
    calculate_ancestral_lines,
)

from .purpose import (
    calculate_personal_purpose,
    calculate_social_purpose,
    calculate_spiritual_purpose,
    calculate_planetary_purpose,
)

from .inner import (
    InnerPoints,
    calculate_inner_points,
)

from .zones import (
    WellbeingPoints,
    ThematicZones,
    calculate_wellbeing_points,
    calculate_thematic_zones,
)

from .ancestral_programs import (
    AncestralPrograms,
    calculate_ancestral_programs,
)

from .heart import (
    HeartPoints,
    calculate_heart_points,
)

from .chakras import (
    ChakraChart,
    ChakraTotals,
    calculate_chakras,
    calculate_chakra_totals,
)


@dataclass(frozen=True, slots=True)
class DestinyMatrix:
    """Объединённый результат расчёта матрицы."""

    personal: PersonalSquare
    ancestral: AncestralSquare

    @property
    def lines(self) -> PersonalLines:
        """Линии Неба и Земли."""
        return calculate_personal_lines(self.personal)

    @property
    def ancestral_lines(self) -> AncestralLines:
        """Родовые линии отца и матери."""
        return calculate_ancestral_lines(self.ancestral)

    @property
    def personal_purpose(self) -> int:
        """Личное предназначение."""
        return calculate_personal_purpose(self.lines)

    @property
    def social_purpose(self) -> int:
        """Социальное предназначение."""
        return calculate_social_purpose(
            self.ancestral_lines
        )

    @property
    def spiritual_purpose(self) -> int:
        """Духовное предназначение."""
        return calculate_spiritual_purpose(
            self.personal_purpose,
            self.social_purpose,
        )

    @property
    def planetary_purpose(self) -> int:
        """Планетарное предназначение."""
        return calculate_planetary_purpose(
            self.social_purpose,
            self.spiritual_purpose,
        )

    @property
    def inner_points(self) -> InnerPoints:
        """Восемь внутренних точек личного квадрата."""
        return calculate_inner_points(self.personal)

    @property
    def wellbeing(self) -> WellbeingPoints:
        """Точки отношений и финансов."""
        return calculate_wellbeing_points(
            self.inner_points
        )

    @property
    def zones(self) -> ThematicZones:
        """Тематические зоны матрицы."""
        return calculate_thematic_zones(
            self.personal,
            self.inner_points,
            self.wellbeing,
        )

    @property
    def ancestral_programs(self) -> AncestralPrograms:
        """Родовые программы через личный центр Д."""
        return calculate_ancestral_programs(
            self.ancestral,
            self.personal.center,
        )

    @property
    def heart_points(self) -> HeartPoints:
        """Дополнительные точки Ъ и Ь."""
        return calculate_heart_points(
            self.inner_points,
            self.personal.center,
        )

    @property
    def chakras(self) -> ChakraChart:
        """Рассчитать таблицу семи чакр."""
        return calculate_chakras(
            self.personal,
            self.inner_points,
            self.heart_points,
        )

    @property
    def chakra_totals(self) -> ChakraTotals:
        """Итоговые значения чакральной таблицы."""
        return calculate_chakra_totals(
            self.chakras
        )


def calculate_destiny_matrix(
    birth_date: date,
) -> DestinyMatrix:
    """Рассчитать Матрицу Судьбы по дате рождения."""

    personal = calculate_personal_square(birth_date)
    ancestral = calculate_ancestral_square(personal)

    return DestinyMatrix(
        personal=personal,
        ancestral=ancestral,
    )
