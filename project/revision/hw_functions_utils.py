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
    discount = 0
    if age < 6:
        discount = BASE_PRICE * 1
    if 6 <= age <= 17:
        discount = BASE_PRICE * 0.5
    if 18 <= age <= 59:
        discount = BASE_PRICE * 0
    if 60 <= age:
        discount = BASE_PRICE * 0.3
    return BASE_PRICE - discount
