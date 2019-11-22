#пишем код из 3.2.12 в утрощенном виде для PyTest


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

