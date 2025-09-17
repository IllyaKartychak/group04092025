from revision.function_utils import is_number_bigger_than_given, add_salt_to_list
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

    result = is_number_bigger_than_given(candidate_number=66, threshold=1)
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


if __name__ == "__main__":
    main()
