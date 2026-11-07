def reverse_string(text):
    reverse = ""

    for ch in text:
        reverse = ch + reverse

    return reverse


def test_hello():
    assert reverse_string("hello") == "olleh"


def test_python():
    assert reverse_string("python") == "nohtyp"


def test_apple():
    assert reverse_string("apple") == "elppa"


def test_empty_string():
    assert reverse_string("") == ""


def test_single_character():
    assert reverse_string("A") == "A"


def test_numbers():
    assert reverse_string("12345") == "54321"