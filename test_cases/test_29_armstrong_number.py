import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_armstrong_number():
    assert is_armstrong(153) == True


def test_not_armstrong_number():
    assert is_armstrong(123) == False


def test_single_digit_number():
    assert is_armstrong(5) == True


def test_negative_number():
    assert is_armstrong(-153) == False
