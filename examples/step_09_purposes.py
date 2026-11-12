
"""Консольный отчёт по Матрице Судьбы."""

from esoterica.core import parse_birth_date

from esoterica.systems.destiny_matrix import (
    calculate_destiny_matrix,
)


def main():
    while True:
        source = input(
            "Введите дату рождения (ДД.ММ.ГГГГ): "
        )

        try:
            birth_date = parse_birth_date(source)
            break
        except ValueError as error:
            print(f"Ошибка: {error}")

    matrix = calculate_destiny_matrix(birth_date)

    print("\n=== МАТРИЦА СУДЬБЫ ===")
    print(f"Дата рождения: {birth_date:%d.%m.%Y}")

    print("\n--- КВАДРАТЫ ---")
    print("Личный:", matrix.personal)
    print("Родовой:", matrix.ancestral)

    print("\n--- ЛИЧНЫЕ ЛИНИИ ---")
    print("Небо:", matrix.lines.heaven)
    print("Земля:", matrix.lines.earth)

    print("\n--- РОДОВЫЕ ЛИНИИ ---")
    print("Линия отца:", matrix.ancestral_lines.father)
    print("Линия матери:", matrix.ancestral_lines.mother)

    print("\n--- ПРЕДНАЗНАЧЕНИЯ ---")
    print("Личное:", matrix.personal_purpose)
    print("Социальное:", matrix.social_purpose)
    print("Духовное:", matrix.spiritual_purpose)
    print("Планетарное:", matrix.planetary_purpose)


if __name__ == "__main__":
    main()
