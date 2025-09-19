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


BASE_PRICE = 100


def get_ticket_price(age: int) -> float:
    if age < 6:
        return 0
    if 6 <= age <= 17:
        discount = BASE_PRICE * 0.5
        return BASE_PRICE - discount
    if 18 <= age <= 59:
        return BASE_PRICE
    if 60 <= age:
        discount = BASE_PRICE * 0.3
        return BASE_PRICE - discount
