from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("hi there") == 20
    assert value("Hi there") == 20
    assert value("HI THERE") == 20

def test_default():
    assert value("Enjoy your day") == 100
    assert value("Enjoy Your Day") == 100
    assert value("ENJOY YOUR DAY") == 100

