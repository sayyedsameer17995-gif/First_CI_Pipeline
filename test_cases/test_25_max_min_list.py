import importlib
import pytest

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_normal_list():
    assert find_max_min([10, 5, 20, 3, 15]) == (20, 3)


def test_same_numbers():
    assert find_max_min([5, 5, 5]) == (5, 5)


def test_negative_numbers():
    assert find_max_min([-10, -5, -20]) == (-5, -20)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])
