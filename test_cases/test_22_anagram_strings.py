
import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram


def test_basic_anagram():
    assert is_anagram("listen", "silent") == True


def test_anagram_with_different_case():
    assert is_anagram("Triangle", "Integral") == True


def test_not_anagram():
    assert is_anagram("hello", "world") == False


def test_anagram_with_spaces():
    assert is_anagram("Dormitory", "Dirty room") == True

