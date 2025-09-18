from revision.function_utils import is_number_bigger_than_given, add_salt_to_list
from revision.hw_functions import greet_person, is_even, reverse_string, calculate_average, add_person_to_list, \
    count_vowels, fahrenheit_to_celsius
from revision.hw_functions_utils import get_string, get_multiply_of_numbers, get_biggest_number_from_list
from services.logger import logger


def main():
    result = is_number_bigger_than_given(candidate_number=5)
    logger.info(f"Function is_number_bigger_than_given was called", extra={
        "candidate_number": 5,
        "result": result

    })
    logger.debug(f"Function is_number_bigger_than_given was called", extra={
        "candidate_number": 5,
        "result": result

    })
    logger.error(f"Function is_number_bigger_than_given was called", extra={
        "candidate_number": 5,
        "result": result

    })

    string = get_string(string="Hello, buddy")
    logger.info(string)

    numbers_function = get_multiply_of_numbers(number1=23, number2=40)
    logger.info(numbers_function)

    numbers = get_biggest_number_from_list(numbers=["abs", 5])
    logger.info(numbers)

    given_list = []
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)

    person_name = greet_person(name="Alex")
    logger.info(f"Function greet_person was called", extra={
        "name": "Alex",
        "result": person_name
    })

    number = is_even(number=5)
    logger.info(number)

    text = reverse_string(text="hello world")
    logger.info(text)

    average_numbers = calculate_average(numbers=[1, 2])
    logger.info(average_numbers)

    people = add_person_to_list(people=["Mark", "Alex", "Ivan"], person="Vasya")
    logger.info(people)

    vowels_counter = count_vowels(text="hrywergtrefhrпіпівпйупавоп")
    logger.info(vowels_counter)

    celsius = fahrenheit_to_celsius(fahrenheit=546)
    logger.info(celsius)

    if __name__ == "__main__":
        main()
