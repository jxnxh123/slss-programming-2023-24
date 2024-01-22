# Chip rater
# Author: jonah 

# 1 November 2023

# Interview people about their
# perception of how delicous chips are
# based on a set of questions
# In the end, we'll give an aggregate score.

# Greet the user
print("please answer the following qustions based on the chip that you just ate")
# create a list of questions to ask
questions = [
    "how crispy is the chip on a scale from 1 to 5? 5 is very cripsy. 1 is mushy,",
    "how would you rate the taste for 1 to 5? 5 is the best taste ever. 1 is id rather eat dirt",
    "from 1 to 5, how would you rate the packaging? 5 is id buy this just for the packaging, 1 is someone got paid for this?  "

]

final_score = 0
# Ask the questions to the user
for question in questions:
    print(question)
    
    # store their response
    rating = int(input().strip(",.?! "))
    final_score += rating 

# do some math - average 
average_score = final_score / len(questions)

# present the results the user
print(f"the average score of this chip is: {average_score:.2f} / 5")