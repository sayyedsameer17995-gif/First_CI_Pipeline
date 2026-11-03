import importlib

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list


def test_normal_list():
    assert sum_of_list([10, 20, 30, 40]) == 100


def test_empty_list():
    assert sum_of_list([]) == 0


def test_negative_numbers():
    assert sum_of_list([-5, -10, 15]) == 0


def test_single_element():
    assert sum_of_list([25]) == 25
