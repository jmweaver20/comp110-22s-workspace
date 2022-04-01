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
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the values attribute with a range of values in terms of floats."""
        assert step != 0.0
        self.values.append(start)
        range: float = (stop / step)
        i: int = 1
        while (i < (range - 1)):
            self.values.append(self.values[i - 1] + step)
            i += 1
        # too many values printed in the ipynb?; why does decimal one print whole numbers?
    
    def sum(self) -> float:
        """Computes sum of simpy."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Takes two parameters of simpy or float type and adds them together returning 1 simpy."""
        combined: Simpy = Simpy([])

        # doesn't work if it's a simpy? prints empty list?
        if (isinstance(rhs, Simpy)):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while (i < len(self.values)):
                combined.values.append(self.values[i] + rhs.values[i])
                i += 1
        elif (isinstance(rhs, float)):
            i: int = 0
            while (i < len(self.values)):
                combined.values.append(self.values[i] + rhs) 
                i += 1
        return combined