from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("77/100") == 77
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    with pytest.raises(ValueError):
        convert("error/error")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
