from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        assert convert("llama/ostrich")
    with pytest.raises(ValueError):
        assert convert("4/3")
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(45) == "45%"
