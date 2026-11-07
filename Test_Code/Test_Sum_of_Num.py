def sum_of_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total


def test_sum_123():
    assert sum_of_digits(123) == 6


def test_sum_456():
    assert sum_of_digits(456) == 15


def test_sum_789():
    assert sum_of_digits(789) == 24


def test_sum_100():
    assert sum_of_digits(100) == 1


def test_sum_0():
    assert sum_of_digits(0) == 0


def test_sum_555():
    assert sum_of_digits(555) == 15