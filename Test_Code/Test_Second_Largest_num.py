def second_largest(numbers):
    largest = second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return None

    return second


def test_list_1():
    assert second_largest([10, 20, 30, 40, 50]) == 40


def test_list_2():
    assert second_largest([5, 8, 2, 10, 6]) == 8


def test_list_3():
    assert second_largest([100, 50, 30]) == 50


def test_list_4():
    assert second_largest([10, 10, 5]) == 5


def test_list_5():
    assert second_largest([5]) == None


def test_list_6():
    assert second_largest([7, 7, 7]) == None