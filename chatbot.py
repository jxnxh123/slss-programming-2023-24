# Chatbot
# Author: Jonah
# Date: 20 september 2023

import random
import time


# Greet the user
print (" hello there! 🥰😜")
# Pause for 1.5 seconds
time.sleep(1.5)

print ("I am crude chatbot, here to talk to you! ")
time.sleep(1.5)
# Get the users name and store it in a variable
user_name = input ("so...whats your name? ")


# Respond with the user's name in a friendly way

print (f" It's good to meet you, {user_name}. ")

# Ask the user what their favourte food is
fave_food = input("What's your favourite food? ")

# Make a comment about their favourite food
# Create a list of possible responses 
list_of_food_responses = [
    f"Oh. Iv'e never had {fave_food} before.",
    "Mmmmm. That sounds good!",
    "Cool."
]
# Choose one of those repsonses randomly

random_food_response = random.choice(list_of_food_responses)
# Print out that random repsonse 
print(random_food_response)

print(list_of_food_responses[2])

# Print out that chosen response
