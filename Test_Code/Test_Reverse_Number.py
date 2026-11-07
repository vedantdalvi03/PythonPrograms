def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse


def test_reverse_123():
    assert reverse_number(123) == 321


def test_reverse_456():
    assert reverse_number(456) == 654


def test_reverse_100():
    assert reverse_number(100) == 1


def test_reverse_1234():
    assert reverse_number(1234) == 4321


def test_reverse_0():
    assert reverse_number(0) == 0


def test_reverse_single_digit():
    assert reverse_number(5) == 5