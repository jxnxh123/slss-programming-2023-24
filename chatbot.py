# Chatbot
# Author: Jonah
# Date: 20 september 2023

# Greet the user
print (" hello there! 🥰😜")
print ("I am crude chatbot, here to talk to you! ")
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
import random
random_food_response = random.choice(list_of_food_responses)
# Print out that random repsonse 
print(random_food_response)

# Print out that chosen response
