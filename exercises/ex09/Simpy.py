"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730397253"


class Simpy:
    """Simplified version of NumPY in Python."""
    values: list[float]

    def __init__(self, vals: list[float]):
        """Takes parameter of float values and initializes to a new Simpy object."""
        self.values = vals
    
    def __str__(self) -> str:
        """Returns string representation of simpy."""
        return f"Simpy({self.values})"
    
    def fill(self, filler: float, num: int) -> None:
        """Fills a simpy's values with filler values num amount of times."""
        
        if len(self.values) == 0:
            self.values.append(filler)
        else:
            self.values[0] = filler
        
        i: int = 1
        while (i < len(self.values)):
            self.values[i] = filler
            i += 1
        if (len(self.values) > num):
            while (len(self.values) > num):
                self.values.pop()
        if i < num:
            while (i < num):
                self.values.append(filler)
                i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the values attribute with a range of values in terms of floats."""
        assert step != 0.0
        if (start < stop):
            while (start < stop):
                self.values.append(start)
                start += step
        else:
            while (start > stop):
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Computes sum of simpy."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Takes two parameters of simpy or float type and adds them together returning 1 simpy."""
        combined: Simpy = Simpy([])

        if (isinstance(rhs, float)):
            i: int = 0
            while (i < len(self.values)):
                combined.values.append(self.values[i] + rhs) 
                i += 1
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while (i < len(self.values)):
                combined.values.append(self.values[i] + rhs.values[i])
                i += 1
        return combined
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Takes two parameters of simpy or float and raises to the power returning a simpy."""
        combined: Simpy = Simpy([])

        if (isinstance(rhs, float)):
            i: int = 0
            while (i < len(self.values)):
                combined.values.append(self.values[i] ** rhs)
                i += 1
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while (i < len(self.values)):
                combined.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return combined
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces mask based on equality of each item in values with another simpy or float."""
        mask: list[bool] = []
        
        if (isinstance(rhs, float)):
            i: int = 0
            while (i < len(self.values)):
                if (self.values[i] == rhs):
                    mask.append(True)
                else:
                    mask.append(False)
                i += 1
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while (i < len(self.values)):
                if (self.values[i] == rhs.values[i]):
                    mask.append(True)
                else:
                    mask.append(False)
                i += 1
        return mask
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a mask of values greater than the float or simpy object passed."""
        mask: list[bool] = []
        if (isinstance(rhs, float)):
            i: int = 0
            while (i < len(self.values)):
                if (self.values[i] > rhs):
                    mask.append(True)
                else:
                    mask.append(False)
                i += 1
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while (i < len(self.values)):
                if (self.values[i] > rhs.values[i]):
                    mask.append(True)
                else:
                    mask.append(False)
                i += 1
        return mask
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription notation with simpy objects, or select for certain values."""
        mask_vals: Simpy = Simpy([])

        if (isinstance(rhs, int)):
            return self.values[rhs]
        else:
            i: int = 0
            while (i < len(self.values)):
                if(rhs[i]):
                    mask_vals.values.append(self.values[i])
                i += 1
        return mask_vals