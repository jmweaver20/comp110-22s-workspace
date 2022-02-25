"""Test file for the dictionary file (ex06)."""

__author__ = "730397253"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_order() -> None:
    """Ensures that invert function inverts the input parameters. Use Case."""
    test_val: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(test_val) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_invert_one() -> None:
    """Ensures that if the dict is one value, it is inverted. Use Case."""
    test_val: dict[str, str] = {'a': 'b'}
    assert invert(test_val) == {'b': 'a'}


def test_invert_keyerror() -> None:
    """Ensures that function raises error if duplicate keys. Edge Case."""
    with pytest.raises(KeyError):
        test_val: dict[str, str] = {'a': 'b', 'c': 'b'}
        invert(test_val)

