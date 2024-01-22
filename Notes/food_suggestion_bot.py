# Food Suggestion Bot
# Author: Ubial
# 6 October 2023

# A bot that asked the user what their favourite 
#food is. Based on that food, it will classify
# the type/genre/cuisine of the food, then
# Give a restaurant suggestion.

# Introdice the bot to the user
# Ask the user what their favourite food is
import random
import time


print("Hello, I am here to suggest you a restaurant. ")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favourite food is. ")
time.sleep(1)

#  Italian Cuisine 
italian_food = ["pasta", "pizza", "canneloni",]
# Japanese cuisine
japanese_food = ["sushi", "ramen", "gyoza",]
# Add another cuisine that our bot should make a suggestion for
# If they answer with Italian food,
# Suggest an Italian restaurant 
if fave_food.lower().strip("!.,") in italian_food:
    print("I suggest broli kitchen. ")
    time.sleep(1)
    print("186-8180 No 2 Rd, Richmond, BC V7C 5K1")
# if they answer with japanese food,
# suggest a japanese restaurant 
elif fave_food.lower().strip("!.,?") in japanese_food:
    print(" I suggest otaru japanese kitchen. ")
    time.sleep(1)
    print("8180 No 2 Rd #168, Richmond, BC V7C 5K1")
else:
    print("sorry, im not sure what kind of food that is. ")
    time.sleep(1)


