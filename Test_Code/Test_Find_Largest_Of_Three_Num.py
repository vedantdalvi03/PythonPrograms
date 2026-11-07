def test_find_largest():
    assert find_largest(10, 20, 30) == 30
    assert find_largest(50, 20, 30) == 50
    assert find_largest(10, 40, 30) == 40
    assert find_largest(5, 5, 5) == 5
    assert find_largest(-10, -20, -5) == -5

    print("All tests passed!")


def find_largest(a, b, c):
    return max(a, b, c)


test_find_largest() 