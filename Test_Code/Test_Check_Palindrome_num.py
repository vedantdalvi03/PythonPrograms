def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse


def test_palindrome_121():
    assert is_palindrome(121) == True


def test_palindrome_madam():
    assert is_palindrome(131) == True


def test_not_palindrome_123():
    assert is_palindrome(123) == False


def test_palindrome_22():
    assert is_palindrome(22) == True


def test_palindrome_0():
    assert is_palindrome(0) == True


def test_single_digit():
    assert is_palindrome(5) == True