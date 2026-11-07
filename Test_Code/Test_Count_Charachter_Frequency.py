def count_frequency(text):
    frequency = {}

    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    return frequency


def test_hello():
    assert count_frequency("hello") == {
        'h': 1, 'e': 1, 'l': 2, 'o': 1
    }


def test_apple():
    assert count_frequency("apple") == {
        'a': 1, 'p': 2, 'l': 1, 'e': 1
    }


def test_banana():
    assert count_frequency("banana") == {
        'b': 1, 'a': 3, 'n': 2
    }


def test_empty_string():
    assert count_frequency("") == {}


def test_single_character():
    assert count_frequency("a") == {'a': 1}


def test_numbers():
    assert count_frequency("11223") == {
        '1': 2, '2': 2, '3': 1
    }