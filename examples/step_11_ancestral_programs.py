
"""Отчёт по четырём родовым программам."""

from esoterica.core import parse_birth_date

from esoterica.systems.destiny_matrix import (
    calculate_destiny_matrix,
)


def format_program(program):
    """Представить тройку энергий через дефис."""

    return "-".join(str(value) for value in program.energies)


def main():
    source = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
    birth_date = parse_birth_date(source)

    matrix = calculate_destiny_matrix(birth_date)
    programs = matrix.ancestral_programs

    print("\n=== РОДОВЫЕ КАНАЛЫ ===")
    print(f"Дата: {birth_date:%d.%m.%Y}")
    print(f"Личный центр Д: {matrix.personal.center}")

    print(
        "Мужской род, духовное:",
        format_program(programs.father_spiritual),
    )
    print(
        "Женский род, духовное:",
        format_program(programs.mother_spiritual),
    )
    print(
        "Мужской род, материальное:",
        format_program(programs.father_material),
    )
    print(
        "Женский род, материальное:",
        format_program(programs.mother_material),
    )


if __name__ == "__main__":
    main()
