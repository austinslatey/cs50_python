from numb3rs import validate

def test_valid_ipv4():
    assert validate("192.168.1.1") == True

def test_invalid_ipv4():
    assert validate("275.3.6.28") == False

def test_partial_valid_ipv4():
    assert validate("192.256.300.400") == False
