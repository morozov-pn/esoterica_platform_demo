
"""Консольный отчёт: чакры и варны с учётом времени."""

from datetime import datetime, time

from esoterica.core import parse_birth_date

from esoterica.systems.destiny_matrix import (
    calculate_destiny_matrix,
)

from esoterica.systems.varna_numerology import (
    calculate_varna_profile,
)


def read_birth_time() -> time | None:
    """Запросить время рождения или вернуть None."""

    while True:
        source = input(
            "Время рождения (ЧЧ:ММ, Enter — неизвестно): "
        ).strip()

        if not source:
            return None

        try:
            # Принимаем строго пять символов: 00:15.
            if len(source) != 5 or source[2] != ":":
                raise ValueError("Неверный формат")

            return datetime.strptime(
                source, "%H:%M"
            ).time()

        except ValueError:
            print(
                "Ошибка: введи время в формате ЧЧ:ММ, "
                "например 00:15 или 14:30."
            )


def print_chakras(matrix):
    """Вывести точки Анахаты и таблицу семи чакр."""

    heart = matrix.heart_points
    chart = matrix.chakras
    totals = matrix.chakra_totals

    print("\n--- ДОПОЛНИТЕЛЬНЫЕ ТОЧКИ ---")
    print("Ъ (левая ось):", heart.hard_sign)
    print("Ь (верхняя ось):", heart.soft_sign)

    print("\n--- АНАХАТА ---")
    print("Физика:", chart.anahata.physical)
    print("Энергия:", chart.anahata.energy)
    print("Эмоции:", chart.anahata.emotions)

    print("\n--- КАРТА СЕМИ ЧАКР ---")

    print(
        f"{'Чакра':<17}"
        f"{'Физика':>9}"
        f"{'Энергия':>10}"
        f"{'Эмоции':>10}"
    )

    print("-" * 46)

    rows = (
        ("Сахасрара", chart.sahasrara),
        ("Аджна", chart.ajna),
        ("Вишудха", chart.vishuddha),
        ("Анахата", chart.anahata),
        ("Манипура", chart.manipura),
        ("Свадхистана", chart.svadhisthana),
        ("Муладхара", chart.muladhara),
    )

    for name, row in rows:
        print(
            f"{name:<17}"
            f"{row.physical:>9}"
            f"{row.energy:>10}"
            f"{row.emotions:>10}"
        )

    print("-" * 46)

    print(
        f"{'Сумма':<17}"
        f"{totals.raw_physical:>9}"
        f"{totals.raw_energy:>10}"
        f"{totals.raw_emotions:>10}"
    )

    print(
        f"{'Итог':<17}"
        f"{totals.physical:>9}"
        f"{totals.energy:>10}"
        f"{totals.emotions:>10}"
    )


def print_varnas(birth_date, birth_time):
    """Вывести варны с информацией о поправке на время."""

    profile = calculate_varna_profile(
        birth_date,
        birth_time,
    )

    print("\n--- РАСЧЁТ ВАРН ---")

    print(
        "Фактическая дата:",
        f"{profile.birth_date:%d.%m.%Y}",
    )

    if profile.birth_time is None:
        print("Время рождения: неизвестно")
    else:
        print(
            "Время рождения:",
            f"{profile.birth_time:%H:%M}",
        )

    print(
        "Дата для расчёта:",
        f"{profile.calculation_date:%d.%m.%Y}",
    )

    if profile.adjustment_applied:
        print("Поправка: предыдущий календарный день")
    else:
        print("Поправка: не применялась")

    print("\nСоставляющие:")

    components = (
        ("День", profile.day),
        ("Месяц", profile.month),
        ("Год", profile.year),
        ("Итог", profile.total),
    )

    for name, factor in components:
        print(
            f"{name:<8}"
            f"Число: {factor.digit}  "
            f"Варна: {factor.varna.value:<10} "
            f"Вес: {factor.percent}%"
        )

    print("\nРаспределение по варнам:")

    for varna, percent in profile.shares.items():
        print(f"  {varna.value:<10} {percent}%")

    print("\nЧисло экспрессии:", profile.expression_digit)
    print("Варна экспрессии:", profile.expression_varna.value)


def main():
    """Получить дату, время и вывести оба расчёта."""

    while True:
        source = input(
            "Введите дату рождения (ДД.ММ.ГГГГ): "
        )

        try:
            birth_date = parse_birth_date(source)
            break
        except ValueError as error:
            print(f"Ошибка: {error}")
            print("Повторите ввод.")

    birth_time = read_birth_time()

    # Матрица Судьбы использует фактическую дату.
    matrix = calculate_destiny_matrix(birth_date)

    print("\n=== ЭЗОТЕРИЧЕСКИЕ РАСЧЁТЫ ===")
    print(f"Дата рождения: {birth_date:%d.%m.%Y}")

    print_chakras(matrix)
    print_varnas(birth_date, birth_time)

    print("\nРасчёт завершён.")


if __name__ == "__main__":
    main()
