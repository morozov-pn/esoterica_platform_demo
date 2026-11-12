
"""Расширенный консольный отчёт по Матрице Судьбы."""

from esoterica.core import parse_birth_date

from esoterica.systems.destiny_matrix import (
    calculate_destiny_matrix,
)


def format_triplet(values: tuple[int, int, int]) -> str:
    """Преобразовать три энергии в строку через дефис."""

    return "-".join(str(value) for value in values)


def main():
    """Запросить дату рождения и вывести расчёт матрицы."""

    while True:
        source = input(
            "Введите дату рождения (ДД.ММ.ГГГГ): "
        )

        try:
            birth_date = parse_birth_date(source)
            break

        except ValueError as error:
            print(f"Ошибка: {error}")
            print("Попробуйте ещё раз.")

    # Выполняем полный доступный расчёт.
    matrix = calculate_destiny_matrix(birth_date)

    print("\n================================")
    print("        МАТРИЦА СУДЬБЫ")
    print("================================")

    print(f"Дата рождения: {birth_date:%d.%m.%Y}")

    # Базовые квадраты.
    print("\n--- БАЗОВЫЕ ТОЧКИ ---")

    print("Личный квадрат:", matrix.personal)
    print("Родовой квадрат:", matrix.ancestral)

    # Внутренние точки.
    print("\n--- ВНУТРЕННИЕ ТОЧКИ ---")

    for name, axis in (
        ("Верх", matrix.inner_points.top),
        ("Право", matrix.inner_points.right),
        ("Низ", matrix.inner_points.bottom),
        ("Лево", matrix.inner_points.left),
    ):
        print(
            f"{name}: "
            f"у центра={axis.near_center}, "
            f"у края={axis.near_outer}"
        )

    # Линии Неба и Земли.
    print("\n--- ЛИНИИ НЕБА И ЗЕМЛИ ---")

    print("Небо:", matrix.lines.heaven)
    print("Земля:", matrix.lines.earth)

    # Родовые линии.
    print("\n--- РОДОВЫЕ ЛИНИИ ---")

    print("Линия отца:", matrix.ancestral_lines.father)
    print("Линия матери:", matrix.ancestral_lines.mother)

    # Отношения и финансы.
    print("\n--- ЛИНИЯ ОТНОШЕНИЙ И ФИНАНСОВ ---")

    print("Баланс:", matrix.wellbeing.balance)
    print("Отношения:", matrix.wellbeing.relationship)
    print("Деньги:", matrix.wellbeing.money)

    # Тематические зоны.
    print("\n--- ТЕМАТИЧЕСКИЕ ЗОНЫ ---")

    zones = matrix.zones

    print(
        "Таланты:",
        format_triplet(zones.talents),
    )

    print(
        "Кармический хвост:",
        format_triplet(zones.karmic_tail),
    )

    print(
        "Материальная карма:",
        format_triplet(zones.material_karma),
    )

    print(
        "Детско-родительская зона:",
        format_triplet(zones.parent_child),
    )

    print(
        "Отношения:",
        format_triplet(zones.relationships),
    )

    print(
        "Финансы:",
        format_triplet(zones.money),
    )

    # Предназначения.
    print("\n--- ПРЕДНАЗНАЧЕНИЯ ---")

    print("Личное:", matrix.personal_purpose)
    print("Социальное:", matrix.social_purpose)
    print("Духовное:", matrix.spiritual_purpose)
    print("Планетарное:", matrix.planetary_purpose)

    print("\n================================")
    print("       РАСЧЁТ ЗАВЕРШЁН")
    print("================================")


if __name__ == "__main__":
    main()
