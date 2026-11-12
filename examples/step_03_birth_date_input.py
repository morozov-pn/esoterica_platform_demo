"""Пример расчёта личного квадрата по текстовой дате рождения."""

from esoterica.core import parse_birth_date
from esoterica.systems.destiny_matrix import calculate_personal_square


if __name__ == "__main__":
    source = "04.05.1986"
    birth_date = parse_birth_date(source)
    square = calculate_personal_square(birth_date)

    print(f"Дата рождения: {source}")
    print(
        f"левая={square.left}, верхняя={square.top}, "
        f"правая={square.right}, нижняя={square.bottom}, "
        f"центр={square.center}"
    )

