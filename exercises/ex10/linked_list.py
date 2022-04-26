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
        # this will reset max val to last value of linked list ??
        max_val: int
        if head.next is None:
            max_val = head.data
            return max_val
        else:
            max_val = head.data
            if head.data > max_val:
                max_val = head.data
            return max(head.next)


def linkify(items: list[int]) -> Optional[Node]:

    if (len(items) == 0):
        return None
    else:
        # how can i do this without hard coding numbers
        linked: Node = Node()
        linked.data = items[0]
        linked.next = linkify(items[0 + 1])
        return linked