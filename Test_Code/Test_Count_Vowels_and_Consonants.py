def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


def test_hello():
    assert count_vowels_consonants("hello") == (2, 3)


def test_python():
    assert count_vowels_consonants("python") == (1, 5)


def test_education():
    assert count_vowels_consonants("education") == (5, 4)


def test_apple():
    assert count_vowels_consonants("apple") == (2, 3)


def test_empty_string():
    assert count_vowels_consonants("") == (0, 0)


def test_numbers_and_symbols():
    assert count_vowels_consonants("abc123!") == (1, 2)