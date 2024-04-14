from hello import hello

def test_hello():
    hello("David") == "hello, David"


def test_default():
    hello() == "hello, world"
