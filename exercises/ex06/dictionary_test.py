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


def test_favorite_color() -> None:
    """Tests that function returns favorite colors according to count. Use Case."""
    test_val: dict[str, str] = {'bob': 'blue', 'richard': 'red', 'lily': 'blue'}
    assert favorite_color(test_val) == 'blue'


def test_favorite_color_duplicate() -> None:
    """Ensures if duplicate favorite colors, first occuring one prints. Edge Case."""
    test_val: dict[str, str] = {'bob': 'blue', 'richard': 'red', 'lily': 'blue', 'sarah': 'red'}
    assert favorite_color(test_val) == 'blue'


def test_favorite_color_one() -> None:
    """Ensures that if only one color, that color is returned. Use Case."""
    test_val: dict[str, str] = {'bob': 'blue'}
    assert favorite_color(test_val) == 'blue'


def test_favorite_color_nomax() -> None:
    """Ensures that if there's no favorite color (all diff), return first color. Edge Case."""
    test_val: dict[str, str] = {'bob': 'blue', 'richard': 'yellow', 'lily': 'green'}
    assert favorite_color(test_val) == 'blue'


def test_count_work() -> None:
    """Ensures that count returns a dictionary with counts of repeated values in list. Use Case."""
    test_val: list[str] = ["a", "b", "b", "c", "d", "d"]
    assert count(test_val) == {'a': 1, 'b': 2, 'c': 1, 'd': 2}


def test_count_all_same() -> None:
    """Ensures that if all values are the same, correct count is returned. Edge Case."""
    test_val: list[str] = ["b", "b", "b", "b"]
    assert count(test_val) == {'b': 4}


def test_count_all_diff() -> None:
    """Ensures that if all values are diff, 1 is returned for each. Use Case."""
    test_val: list[str] = ["a", "b", "c", "d"]
    assert count(test_val) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}