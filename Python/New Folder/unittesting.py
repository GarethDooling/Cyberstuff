from unittesting1 import func1

def test_func1():
    assert func1(6) == 12
    assert func1(12) == 24

def test_func1_2():
    assert func1(6) == 10