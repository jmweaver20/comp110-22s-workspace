"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

from numpy import str0

__author__ = "730397253"


class Simpy:
    values: list[float]

    def __init__(self, vals: list[float]):
        """Takes parameter of float values and initializes to a new Simpy object."""
        self.values = vals
    
    def __str__(self) -> str:
        """Returns string representation of simpy."""
        return f"Simpy({self.values})"
    
    def fill(self, filler: float, num: int) -> None:
        """Fills a simpy's values with filler values num amount of times."""
        i: int = 0
        while (i < num):
            self.values.append(filler)
            i += 1
    
    def arrange(self, start: float, stop: float, step: float) -> Simpy:
        """Fills the values attribute with a range of values in terms of floats."""
        assert step != 0.0
        filled: Simpy = Simpy([])
        



