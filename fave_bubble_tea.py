# Bubble tea popularity algoritm
# Author:Jonah
# Date" October 26, 2023

# Ask 5 users whay their favourite bubble tea place it
# prints out a summary of the data

# ------ CONSTANTS

NUM_RESPONDENTS = 5

# ------

coco_likes = 0    # Initialize the variable to 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0


for _ in range(NUM_RESPONDENTS): 
    # Ask the user what their favourite place is 
    # Store that information somewhere
    print("whats your favourite bubble tea place? ")

    fave_place = input().strip(",.?!").lower()

    # tally of counting algo
    # Options Coco, Suntea, chatime, Bubble Queen
    # If they choose any of these options, increase the counter
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1    # alternate to above
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubqueen":
        bubqueen_likes += 1
    # repeat the code above 5 times

# print out a summary
# give the raw score and the raw score as percentage 

print( f"CoCo likes: {coco_likes}")
