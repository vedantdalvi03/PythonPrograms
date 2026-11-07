def remove_duplicates(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique


def test_list_1():
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]


def test_list_2():
    assert remove_duplicates([1, 1, 1, 2, 2]) == [1, 2]


def test_list_3():
    assert remove_duplicates([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]


def test_empty_list():
    assert remove_duplicates([]) == []


def test_single_element():
    assert remove_duplicates([10]) == [10]


def test_all_duplicates():
    assert remove_duplicates([7, 7, 7, 7]) == [7]