def word_frequency(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def test_normal_sentence():
    assert word_frequency("python is easy and python is powerful") == {
        "python": 2,
        "is": 2,
        "easy": 1,
        "and": 1,
        "powerful": 1
    }


def test_repeated_words():
    assert word_frequency("hello hello hello") == {
        "hello": 3
    }


def test_all_unique_words():
    assert word_frequency("I love python") == {
        "I": 1,
        "love": 1,
        "python": 1
    }


def test_empty_sentence():
    assert word_frequency("") == {}


def test_single_word():
    assert word_frequency("python") == {
        "python": 1
    }


def test_case_sensitive():
    assert word_frequency("Python python PYTHON") == {
        "Python": 1,
        "python": 1,
        "PYTHON": 1
    }