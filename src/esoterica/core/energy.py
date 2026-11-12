"""Общие операции с числовыми энергиями."""


def reduce_to_energy(value: int) -> int:
    """Привести положительное целое число к диапазону от 1 до 22.

    Пока число больше 22, функция складывает его десятичные цифры.
    Число 22 сохраняется без изменений.

    Args:
        value: Положительное целое число.

    Returns:
        Число от 1 до 22 включительно.

    Raises:
        TypeError: Если передано не целое число.
        ValueError: Если передано число меньше 1.
    """

    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value должно быть целым числом")

    if value < 1:
        raise ValueError("value должно быть больше нуля")

    while value > 22:
        value = sum(int(digit) for digit in str(value))

    return value

