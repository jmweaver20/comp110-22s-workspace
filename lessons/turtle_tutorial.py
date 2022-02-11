"""Python Turtle Tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()

leo.color(99, 204, 250)
leo.up()
leo.goto(0, 0)
leo.down()
leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()


bob.color(228, 60, 24)
bob.up()
bob.goto(0, 0)
bob.down()
bob.speed(70)
bob.hideturtle()
side_length: int = 300
x: int = 0
while (x < 10):
    bob.forward(side_length)
    bob.left(120)
    x += 1

done()