def fibonacci(n):
    a = 0
    b = 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


def test_fibonacci_5():
    assert fibonacci(5) == [0, 1, 1, 2, 3]


def test_fibonacci_7():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_1():
    assert fibonacci(1) == [0]


def test_fibonacci_0():
    assert fibonacci(0) == []


def test_fibonacci_2():
    assert fibonacci(2) == [0, 1]