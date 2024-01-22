# funtions and turtle
# Author: jonah
# date: november 28 2023

import turtle

burt = turtle.Turtle()

burt.color("lightblue")


def squared(num: float) -> float:
    """takes a number and squares adn returns it."""

    return num ** 2

def draw_square(side_length: int) -> None:
    """Draw a square of a given length."""
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)

burt.speed(0)

# draw squares that grow exponentially
for i in range(40):
    draw_square(squared(i))



turtle.done()