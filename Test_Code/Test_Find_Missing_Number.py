def find_missing(numbers):
    n = len(numbers) + 1

    total = n * (n + 1) // 2

    missing = total - sum(numbers)

    return missing


def test_list_1():
    assert find_missing([1, 2, 3, 5]) == 4


def test_list_2():
    assert find_missing([1, 2, 4, 5]) == 3


def test_list_3():
    assert find_missing([1, 3, 4, 5]) == 2


def test_list_4():
    assert find_missing([2, 3, 4, 5]) == 1


def test_list_5():
    assert find_missing([1, 2, 3, 4]) == 5


def test_list_6():
    assert find_missing([1]) == 2