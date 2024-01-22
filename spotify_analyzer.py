# spotify Anylizer
# Author: Jonah
# date: january 16 2024

import csv 

# create a function that searches through data
# finds all songs from given artist


# open the file
with open("./spotify.csv") as f:


    # ----- Search for all drake songs
    # ----- Use linear search 
    # create a csv reader object``
    csv_reader = csv.DictReader(f)

    # make a list to store all drake songs
    drake_songs = []
    
    # create a counter to store the current line number
    line_num = 0 


    # for every line in the file 
    for line in csv_reader:
        # if its the first line print out all the headings 
        if line_num == 0:
            print("the columns are: ")

            print(", ".join(line))

            for item in line:
                print(item)
            
            line_num += 1
        else:

        # if the artist for this song is drake
            # store the song info in the list
            # ----- artist, song title, danceability
            if "drake" in line['artist'].lower:
        
                drake_songs.append((
                    line['artist'],
                    line['song_title'],
                    line['danceability']
                    ))
                line_num =+ 1

print(drake_songs)


