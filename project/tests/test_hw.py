from revision.hw_functions_utils import get_ticket_price


def test_get_ticket_price_age_1():
    age = 5
    actual_result = get_ticket_price(age=age)
    # actual
    expected_result = 0
    # testing block
    assert actual_result == expected_result


def test_get_ticket_price_age_2():
    age = 6
    actual_result = get_ticket_price(age=age)
    # actual
    expected_result = 50
    # testing block
    assert actual_result == expected_result


def test_get_ticket_price_age_3():
    age = 27
    actual_result = get_ticket_price(age=age)
    # actual
    expected_result = 100
    # testing block
    assert actual_result == expected_result


def test_get_ticket_price_age_4():
    age = 61
    actual_result = get_ticket_price(age=age)
    # actual
    expected_result = 70
    # testing block
    assert actual_result == expected_result
