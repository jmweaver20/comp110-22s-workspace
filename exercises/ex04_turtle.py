"""A turtle representation of a pretty house and sunset."""

__author__ = "730397253"

from turtle import Turtle, colormode, done, Screen
from random import randint
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    bob: Turtle = Turtle()
    leo: Turtle = Turtle()
    
    # Increases turtles to max speed to help scene render faster.
    bob.speed(0)
    leo.speed(0)
    
    # The next two lines allow me to change the color of my screen
    # so that it looks like a "sunset".
    tur = Screen()
    tur.bgcolor(253, 148, 105)

    # Calls all required functions to build the scene described in
    # intro docstring.
    draw_sun(bob, leo, -200.0, 250.0)
    draw_house_base(bob, leo, 0.0, 0.0)
    draw_house_roof(bob, -50, 0, 330)
    add_grass(bob, -425, -275)
    make_door(bob, 75, -275)
    make_clouds(bob, -5, 150)
    make_clouds(bob, -240, 200)
    make_clouds(bob, -110, 120)
    make_clouds(bob, -150, 100)
    make_clouds(bob, 220, 250)
    make_clouds(bob, 250, 230)
    make_clouds(bob, -115, 235)
    done()


def draw_sun(sun: Turtle, outline: Turtle, x: float, y: float) -> None:
    """Function that draws the sun for the picture."""

    # Makes the sun by turning a very small degree amount 
    # 100 times - opted for this instead of circle() because when
    # looking @ sun in real life, doesn't appear to be a perfect circle.
    sun.color(246, 207, 7)
    outline.color(234, 171, 32)
    sun.up()
    sun.goto(x, y)
    sun.down()
    sun.begin_fill()
    i: int = 0
    while (i < 100):
        sun.forward(2)
        sun.right(3.6)
        i += 1
    sun.end_fill()

    # Outlines the sun to add contrast.
    outline.up()
    outline.goto(x, y)
    outline.down()
    i2: int = 0
    while (i2 < 100):
        outline.forward(2)
        outline.right(3.6)
        i2 += 1


def draw_house_base(base: Turtle, windows: Turtle, x: float, y: float) -> None:
    """Draws the base of the house and adds the windows."""
    base.color(75, 53, 17)
    base.up()
    base.goto(x, y)
    base.down()
    base.begin_fill()
    i: int = 0
    while (i < 4):
        base.forward(250)
        base.right(90)
        base.forward(25)
        i += 1
    base.end_fill()

    # Adds windows to the house base, once drawn by calling make_square
    make_square(windows, x + 5, y + -45, 50)
    make_square(windows, x + 175, y + -45, 50)


def draw_house_roof(roof: Turtle, x: float, y: float, length: float) -> None:
    """Draws the roof of the house, adds a 'shadow' to the roof based on a randint number - attempting fun
    grading category."""

    make_triangle(roof, x, y, length)
    i: int = 0
    leng: float = length

    # Adds an element of randomness to repeat the shading on the
    # triangle roof.
    rand_num: int = randint(20, 75)

    roof.begin_fill()
    while (i < rand_num):
        leng = leng * 0.97
        make_triangle(roof, x, y, leng)
        i += 1
    roof.end_fill()


def make_square(square: Turtle, x: float, y: float, width: float) -> None:
    "Draws a square at desired x, y position and desired width."
    square.color(218, 216, 216)
    square.up()
    square.goto(x, y)
    square.down()
    square.begin_fill()
    i: int = 0
    while (i < 4):
        square.forward(width)
        square.right(90)
        i += 1
    square.end_fill()
    

def make_triangle(tri: Turtle, x: float, y: float, length: float) -> None:
    """Draws a triangle at desired x, y position and desired length."""
    tri.color(144, 136, 133)
    tri.up()
    tri.goto(x, y)
    tri.down()
    i: int = 0
    while (i < 3):
        tri.forward(length)
        tri.left(120)
        i += 1


def add_grass(grass: Turtle, x: float, y: float) -> None: 
    """Adds 'grass' to the image as a green rectangle"""
    grass.color(30, 183, 41)
    grass.up()
    grass.goto(x, y)
    grass.down()
    i: int = 0
    grass.begin_fill()
    while (i < 3):
        grass.forward(1200)
        grass.right(90)
        grass.forward(5)
        i += 1
    grass.end_fill()


def make_door(door: Turtle, x: float, y: float) -> None:
    """Function which adds the door to the front of the house."""
    door.up()
    door.goto(x, y)
    door.down()
    door.color(0, 0, 0)
    i: int = 0
    door.begin_fill()

    # % Division used here because I don't want a square, I want a rectangle
    # so the sides will be different lengths (2 sides one length, 2 the other)
    while (i < 4):
        if (i % 2 == 0):
            door.forward(130)
            door.right(90)
        else:
            door.forward(75)
            door.right(90)
        i += 1
    door.end_fill()


def make_circle(circ: Turtle, radius: float) -> None:
    """Function to make a circle of desired radius."""
    circ.color(218, 204, 199)
    circ.begin_fill()
    circ.circle(radius)
    circ.end_fill()


def make_clouds(cloud: Turtle, x: float, y: float) -> None:
    "Function that makes clouds by calling make_circles and overlapping them."
    cloud.up()
    cloud.goto(x, y)
    cloud.down()
    cloud.forward(20)
    i: int = 0
    while (i < 7):
        make_circle(cloud, 20)
        cloud.right(90)
        cloud.forward(2)
        i += 1


if __name__ == "__main__":
    main()