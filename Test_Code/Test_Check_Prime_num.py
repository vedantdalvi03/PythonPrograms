def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def test_prime_7():
    assert is_prime(7) == True


def test_prime_5():
    assert is_prime(5) == True


def test_not_prime_4():
    assert is_prime(4) == False


def test_not_prime_1():
    assert is_prime(1) == False


def test_not_prime_0():
    assert is_prime(0) == False


def test_prime_2():
    assert is_prime(2) == True