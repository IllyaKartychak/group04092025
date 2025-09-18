def greet_person(name: str = "Гість") -> str:
    return f"Привіт, {name}!"


def is_even(number: int) -> bool:
    return number % 2 == 0


def reverse_string(text: str) -> str:
    reversed_string = text[::-1]
    return reversed_string


def calculate_average(numbers: list[float]) -> float:
    summa = 0
    quantity_of_numbers = 0
    for number in numbers:
        summa += number
        quantity_of_numbers += 1
    average = summa / quantity_of_numbers
    return average


def add_person_to_list(people: list[str], person: str) -> list[str]:
    people_list = people + [person]
    return people_list


def count_vowels(text: str) -> int:
    ukrainian_vowels = {"а", "е", "и", "і", "о", "у", "ю", "я", "є", "ї"}
    english_vowels = {"a", "e", "i", "o", "u"}
    ukrainian_count = 0
    english_count = 0
    text_lower = text.lower()

    for letter in text_lower:
        if letter in ukrainian_vowels:
            ukrainian_count += 1
        if letter in english_vowels:
            english_count += 1
    return ukrainian_count + english_count


# °C = (°F - 32) / 1.8


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) / 1.8
    return celsius
