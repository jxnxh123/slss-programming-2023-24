# turtle example
# author: Jonah
# date: November 21 2023

import turtle

# create a turtle that can be moved around the screen

FORWARD_MAGNITUDE = 20

# Make a turtle object
michaelangelo = turtle.Turtle()

# Get some input from the user
print("""To give commands, type:
F - to go forward
L - to turn left
R - to turn right.                  """)
command = input("where should I go?")

# repeat the below forever, or unitl the user says stop
done = False

while not False:
    command = input("where should I go?").strip(",.?!").lower()

    # move the turtle based around that input
    # stop if the user says stop
    if command in["f", "forward"]:
        michaelangelo.forward(FORWARD_MAGNITUDE)
    elif command in ["l", "left"]:
        michaelangelo.left(90)
    elif command in ["r", "right"]:
        michaelangelo.right(90)
    elif command == "stop":
        done= True









