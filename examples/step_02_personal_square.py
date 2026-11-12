"""Небольшой пример расчёта личного квадрата."""

from datetime import date

from esoterica.systems.destiny_matrix import calculate_personal_square


def show_square(label: str, birth_date: date) -> None:
    square = calculate_personal_square(birth_date)
    print(
        f"{label}: левая={square.left}, верхняя={square.top}, "
        f"правая={square.right}, нижняя={square.bottom}, "
        f"центр={square.center}"
    )


if __name__ == "__main__":
    show_square("23.01.1987", date(1987, 1, 23))
    show_square("04.05.1986", date(1986, 5, 4))

