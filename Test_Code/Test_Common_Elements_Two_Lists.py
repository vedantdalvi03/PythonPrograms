def common_elements(list1, list2):
    common = []

    for num in list1:
        if num in list2 and num not in common:
            common.append(num)

    return common


def test_list_1():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_list_2():
    assert common_elements([1, 2, 3], [4, 5, 6]) == []


def test_list_3():
    assert common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]


def test_list_4():
    assert common_elements([5, 5, 6, 7], [5, 7, 8]) == [5, 7]


def test_empty_list():
    assert common_elements([], [1, 2, 3]) == []


def test_duplicate_elements():
    assert common_elements([1, 1, 2, 2], [1, 2, 3]) == [1, 2]