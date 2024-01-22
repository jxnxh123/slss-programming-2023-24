# McDonalds bot
# author: Jonah
# date: november 5 2023

# ask the user if they want a burger for 5$
user_burger = input(" would you like a burger for $5?")
if user_burger.lower().strip("!,?,.")== "yes": 
    user_burger = 5
    print("ok, that will be $5!")
else: user_burger = 0


# ask if they want to add fries for an extra $3
user_fries = input(" would you like fries for an extra $3?")
if user_fries.lower().strip("!,?,.")== "yes": 
    user_fries = 3
    print("ok, that will be $3! ")
else: user_fries = 0

# caculate the total price


