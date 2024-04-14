from plates import is_valid

def test_valid_plates():
    assert is_valid("AB234") == True
    assert is_valid("XB254") == True
    assert is_valid("ABCD34") == True

def test_invalid_plates():
    assert is_valid("A") == False
    assert is_valid("1234567") == False
    assert is_valid("A##$#!%") == False
    assert is_valid("XY 12") == False

def test_alphabetical():
    assert is_valid("12345") == False


def test_length():
    assert is_valid("AB23456") == False


def test_number_placement():
    assert is_valid("ABCD3E") == False


def test_zero_placement():
    assert is_valid("ABC034") == False


def test_alphanumeric():
    assert is_valid("AB@12") == False
