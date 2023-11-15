# Similar Hobbies
# Author: Jonah
# Date: november 14 2023

# calculate the hobbies between 2 people
# create two lists that represent the hobbies that people have
person1_hobbies = [
    "eating",
    "gaming",
    "sleeping"
]
person2_hobbies = [
    "eating",
    "gaming",
    "bike riding"
]

# initialize the similarity score
similarity_score = 0

# iterate all hobbies in the first list
for hobby in person1_hobbies:
    #if that item is in the second list 
    if hobby in person2_hobbies:
        # increase similarity score by one
        similarity_score += 1

# display the results
print(f"person1 and person2 have a similarity score of {similarity_score}")

