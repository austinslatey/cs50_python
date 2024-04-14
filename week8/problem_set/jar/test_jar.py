from jar import Jar
import pytest

def test_init():
    # Test with default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test with custom capacity
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

def test_str():
    # Test when jar is empty
    jar = Jar()
    assert str(jar) == ""

    # Test when jar has cookies
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()

    # Test depositing cookies within capacity
    jar.deposit(5)
    assert jar.size == 5

    # Test depositing cookies exceeding capacity
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)

    # Test withdrawing cookies
    jar.withdraw(3)
    assert jar.size == 5

    # Test withdrawing more cookies than available
    with pytest.raises(ValueError):
        jar.withdraw(7)
