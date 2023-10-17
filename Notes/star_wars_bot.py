# Star Wars Bot
# Author: Jonah Greaves
# October 16, 2023

import time

# Introduce yourself
print("I am starwars bot")
time.sleep(1)

# Tell them that you will decide if they can join the Dark Side
print("I will decide if you can join the Dark Side.")
time.sleep(1)

# ask if red is their favourite colour
red_colour = input("Is red your favourite colour?")

# ask if they like capes
likes_capes = input("Do you like capes?")

# If yes to one of them or both, they are on Dark Side
# If no to both, they are on the Light Side
if red_colour.lower().strip(".,?!"):
    print("Dark side it is!")
else:
    print("Light Side, I see.")