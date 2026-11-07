def is_palindrome(text):
    reverse = ""

    for ch in text:
        reverse = ch + reverse

    return text == reverse


def test_madam():
    assert is_palindrome("madam") == True


def test_level():
    assert is_palindrome("level") == True


def test_python():
    assert is_palindrome("python") == False


def test_radar():
    assert is_palindrome("radar") == True


def test_empty_string():
    assert is_palindrome("") == True


def test_hello():
    assert is_palindrome("hello") == False