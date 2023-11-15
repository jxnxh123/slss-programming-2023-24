# SFU's best
# Author: Jonah
# date: November 10 2023

# Load Data from .csv file
# read it out in a meaningful way
# link our similarity score to algo to the data

# Open the file
with open( "./data.csv" ) as f:  
    # read the first line of data

    f.readline()
    
# create a profile for someone that shows their
# favourite places at sfu
profile = [
    "Bubble World",
    "Chef Hung",
    "Uncle Fatih's",
    "Guadalupe (MBC)"
    "Steve's Poke Bar"
]

# initialize our top similaity score and their name
top_sim_score = 0
top_sim_name = ""

with open("./data.csv") as f:
    # throw away the header
    header = f.readline()
 # for every line in data in the file (string)
    for line in f: 
    # convert the line of data into a list
        current_likes = line.split(",")
    


    # initializr=e the CURRENT sim score 
    # initialize the persons name
    current_sim_score = 0
    current_name = current_likes[1]

    # sim score algo
    for item in profile:
        if item in current_likes:
            current_sim_score += 1

    # print the current sim_score
    print(f"{current_name}- Score: {current_sim_score}") 

    # if the cur score is > top sim score
    if current_sim_score > top_sim_score: 
        # update the top sim score and name
        top_sim_score = current_sim_score
        top_sim_name = current_name

print("TOP SIMILAR PERSON1!")
print(f"{top_sim_name}- Score: {top_sim_score}")

