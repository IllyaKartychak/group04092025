def get_string(string: str) -> str:
    return string


def get_multiply_of_numbers(number1: float, number2: float) -> float:
    return number1 * number2


def get_biggest_number_from_list(numbers: list) -> float:
    right_numbers = []
    for number in numbers:
        if type(number) is float or type(number) is int:
            right_numbers.append(number)
    if not right_numbers:
        return 0
    return max(right_numbers)
