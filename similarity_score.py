# Comparing similarity scores
# Author: Jonah
# date: November 8 2023

# Calculate the similarity scores between two people 
# Create two lists that represent the movies that people like
Ubials_favourite_movies = [
    "The Matrix",
    "Avengers: Inifinty War",
    "Star wars: The empire strikes back",
    "Infernal Affairs",
    "Rogue One"
]
bens_favourite_movies = [
    "thomas and Friends Big World Big Adventure",
    "Infernal Affairs",
    "rogue One",
    "Spider Man: Into the Spider verse",
    " Gaurdians of the Galaxy: volume 3"
]



# Initialize the similarity score
similarity_score = 0


# Iterate through all movies in first list
for movie in Ubials_favourite_movies:
    # if that item is in the second list
    if movie in bens_favourite_movies:
        # increase the similarity score by 1
        similarity_score += 1

# Display the results
print (f"Ubial and ben have a similarity score of: {similarity_score}")

