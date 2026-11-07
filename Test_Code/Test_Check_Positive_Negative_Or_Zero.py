from Code.Check_Positive_Negative_Or_Zero import check_number

def test_positive():
    assert check_number(10) == "Positive Number"

def test_negative():
    assert check_number(-5) == "Negative Number"

def test_zero():
    assert check_number(0) == "Zero"

def test_positive_decimal():
    assert check_number(2.5) == "Positive Number"

def test_negative_decimal():
    assert check_number(-3.5) == "Negative Number"   