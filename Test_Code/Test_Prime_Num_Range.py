def prime_numbers(start, end):
    primes = []

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)

    return primes


def test_range_1():
    assert prime_numbers(1, 10) == [2, 3, 5, 7]


def test_range_2():
    assert prime_numbers(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_range_3():
    assert prime_numbers(10, 20) == [11, 13, 17, 19]


def test_range_4():
    assert prime_numbers(1, 5) == [2, 3, 5]


def test_range_5():
    assert prime_numbers(8, 10) == []


def test_range_6():
    assert prime_numbers(2, 2) == [2]