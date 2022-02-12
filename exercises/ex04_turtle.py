"""A turtle representation of a pretty house and sunset."""

__author__ = "730397253"

from turtle import Turtle, colormode, done 
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    bob: Turtle = Turtle()
    leo: Turtle = Turtle()
    draw_sun(bob, leo, -200.0, 250.0)
    draw_house_base(bob, leo, 0.0, 0.0)
    done()


def draw_sun(sun: Turtle, outline: Turtle, x: float, y: float) -> None:   # what kind of data type does this return or none?
    """Function that draws the sun for the picture."""
    sun.color(246, 207, 7)
    outline.color(234, 171, 32)
    sun.speed(0)
    outline.speed(0)

    sun.up()
    sun.goto(x, y)
    sun.down()
    sun.begin_fill()
    i: int = 0
    while (i < 100):
        sun.forward(5)
        sun.right(3.6)
        i += 1
    sun.end_fill()

    outline.up()
    outline.goto(x, y)
    outline.down()
    i2: int = 0
    while (i2 < 100):
        outline.forward(5)
        outline.right(3.6)
        i2 += 1


def draw_house_base(base: Turtle, windows: Turtle, x: float, y: float) -> None:
    """Draws the base of the house and adds the windows."""
    base.color(75, 53, 17)
    base.up()
    base.goto(x, y)
    base.down()
    i: int = 0
    while (i < 4):
        base.forward(250)
        base.right(90)
        base.forward(25)
        i += 1
    make_square(windows, x + 5, y + -45)
    make_square(windows, x + 175, y + -45)


def make_square(square: Turtle, x: float, y: float) -> None:
    "Draws a square at desired x, y position."
    square.color(0, 0, 0)
    square.up()
    square.goto(x, y)
    square.down()
    i: int = 0
    while (i < 4):
        square.forward(50)
        square.right(90)
        i += 1
    

if __name__ == "__main__":
    main()