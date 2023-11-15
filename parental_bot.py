# parental bot
# Author: Jonah
# date: November 15 2023

# ask the user what they have done
# make a list of these quations 

questions = [
    "did you eat?",
    "did you study?",
    "did you do your laundry?",
    "did you call grandma?",
]
completed_chores  = 0

# ask the questions to the user
for question in questions:
    print(question)

    # store their response 
    user_response = input().strip(".,!?")

    if user_response == "yes":
        completed_chores += 1

# answer the users questions based on their response 
if completed_chores <= 2:
    print("im coming over!")
elif completed_chores >= 2:
    print("ok")
elif completed_chores >= 4:
    print("good!")


