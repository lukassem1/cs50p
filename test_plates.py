from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("H") == False
    assert is_valid("PI3.14") == False
    assert is_valid("thisisloonnnng") == False
    assert is_valid("AAA11A") == False
    assert is_valid("CS05") == False
    assert is_valid("57FFD") == False
    assert is_valid("32") == False
