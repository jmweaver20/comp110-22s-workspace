"""An example of a class and objects + magic methods and operator overloading."""

from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Constructs a point by giving x and y values."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Special method to represent object as a string."""
        return f"{self.x}, {self.y}"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float"""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, rhs: Point) -> Point:
        """Overload + operator for Point + Point."""
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Index items for point 0 = x, 1 = y."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])