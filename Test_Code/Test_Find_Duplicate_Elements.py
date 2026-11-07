def find_duplicates(numbers):
    duplicates = []

    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    return duplicates


def test_list_1():
    assert find_duplicates([1, 2, 3, 2, 4, 5, 3]) == [2, 3]


def test_list_2():
    assert find_duplicates([1, 1, 2, 2, 3]) == [1, 2]


def test_list_3():
    assert find_duplicates([1, 2, 3, 4, 5]) == []


def test_list_4():
    assert find_duplicates([5, 5, 5, 5]) == [5]


def test_empty_list():
    assert find_duplicates([]) == []


def test_list_5():
    assert find_duplicates([10, 20, 10, 30, 20]) == [10, 20]