from twttr import shorten


def test_removes_vowels():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"


def test_upper_and_lowercase():
    assert shorten("Hello") == "Hll"
    assert shorten("WORLD") == "WRLD"


def test_empty_string():
    assert shorten("") == ""


def test_no_vowels():
    assert shorten("bcd") == "bcd"

def test_preserves_numbers():
    assert shorten("hello123") == "hll123"
    assert shorten("123world") == "123wrld"
    assert shorten("123") == "123"


def test_preserves_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"
