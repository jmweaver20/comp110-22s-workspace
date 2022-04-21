"""Tests for linked list utils."""


from exercises.ex10.linked_list import Node, last, value_at, max
import pytest

__author__ = "730397253"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """value_at with an empty list should raise Index Error."""
    with pytest.raises(IndexError):
        value_at(None, 3)


def test_value_at_full() -> None:
    """value_at with a list should return value at specified index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2
    assert value_at(linked_list, 0) == 1
    assert value_at(linked_list, 2) == 3


def test_max_no_val() -> None:
    """max should raise Value Error if list empty."""
    with pytest.raises(ValueError):
        max(None)


def test_max_with_val() -> None:
    """Max should return greatest value in node list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3
    rev_linked_list = Node(3, Node(2, Node(1, None)))
    assert max(rev_linked_list) == 3