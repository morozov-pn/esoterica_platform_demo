
from esoterica.core import parse_birth_date
from esoterica.systems.destiny_matrix import calculate_personal_square


def main():
    while True:
        source = input("Введите дату рождения (ДД.ММ.ГГГГ): ")

        try:
            birth_date = parse_birth_date(source)
        except ValueError as error:
            print(f"Ошибка: {error}")
            print("Попробуйте ещё раз.")
            continue

        square = calculate_personal_square(birth_date)

        print(f"Дата рождения: {birth_date:%d.%m.%Y}")
        print(
            f"левая={square.left}, верхняя={square.top}, "
            f"правая={square.right}, нижняя={square.bottom}, "
            f"центр={square.center}"
        )
        break


if __name__ == "__main__":
    main()
