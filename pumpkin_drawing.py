# Pumpkin Drawing
# Author: jonah
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle() 
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)


# left eye
carver.setpos(-30, 20)
carver.dot(30)

# right eye
carver.pendown()
carver.setpos(30, 20)
carver.dot(30)


# mouth
carver.penup()
carver.setposition(-30, -30)
carver.pensize(30)
carver.dot(5)
carver.pendown()
carver.forward(100)



# left eyelash
carver.penup()
carver.setposition(80, 80)
carver.pensize(8)
carver.dot(5)


turtle.done()

turtle.done()









