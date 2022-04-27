"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730397253"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if (head.next is None):
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns data at given index or raises error if no index."""
    if head is None:
        raise IndexError("Index is out of bounds on list.")
    else:
        if index == 0:
            return head.data
        else:
            return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns max value of head."""
    if head is None:
        raise ValueError("max cannot be called with empty list.")
    else:
        if head.next is None:
            return head.data
        else:
            max_val: int = max(head.next)
            if head.data > max_val:
                return head.data
            else:
                return max_val


def linkify(items: list[int]) -> Optional[Node]:
    """Links a list of items together into one linked list."""
    if (len(items) == 0):
        return None
    if (len(items) == 1):
        return Node(items[0], None)
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scales a linked list by the factor."""
    if head is None:
        raise ValueError("Scale cannot be called with empty list.")
    else:
        if head.next is None:
            return Node(head.data * factor, None)
        else:
            return Node(head.data * factor, scale(head.next, factor))