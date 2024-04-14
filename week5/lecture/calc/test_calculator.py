from calculator import square
from pytest import raises

def test_postive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with raises(TypeError):
        square("dog")
