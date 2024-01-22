
# Author:
# 21 November 2023

import random 
import turtle

# design a funtion that creates a cookie and x and y
def make_cookie(x: int, y: int ):
    """Creates a cookie on the screen
    draws it at location (x, y
    
    params:
    x - the x-location of the center
    y - the y-location of the center)"""
    baker_turtle.color("brown")
    baker_turtle.penup()
    baker_turtle.goto(-5 + x, -30 + y)
    baker_turtle.pendown()
    baker_turtle.circle(30)
    baker_turtle.peuup()


# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")

# Draw outline of cookie
baker_turtle.penup()
baker_turtle.goto(-5, -30)
baker_turtle.pendown()
baker_turtle.circle(30)
baker_turtle.penup()

# Add chips
baker_turtle.clor("black")
baker_turtle.goto(0, 0)
baker_turtle.stamp()

# add top rigt, bottom right, bottom left, top left
baker_turtle.goto(10, 10)
baker_turtle.stamp()
baker_turtle.goto(10, -10)
baker_turtle.stamp()
baker_turtle.goto(-10, -10)
baker_turtle.stamp()
baker_turtle.goto(-10, 10)
baker_turtle.stamp()


offset = random.radint(-100, 100)


baker_turtle.penup()
baker_turtle.goto(-5, -30)
baker_turtle.pendown()
baker_turtle.circle(30)
baker_turtle.penup()

# Add chips
baker_turtle.clor("black")
baker_turtle.goto(0, 0)
baker_turtle.stamp()

# add top rigt, bottom right, bottom left, top left
baker_turtle.goto(10, 10)
baker_turtle.stamp()
baker_turtle.goto(10, -10)
baker_turtle.stamp()
baker_turtle.goto(-10, -10)
baker_turtle.stamp()
baker_turtle.goto(-10, 10)
baker_turtle.stamp()


turtle.done()

