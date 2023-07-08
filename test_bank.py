from bank import value

def test_value():
    assert value("hello") == 0
    assert value("what's up") == 100
    assert value("hi") == 20
    assert value("HI") == 20

