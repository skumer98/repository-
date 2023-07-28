# Sara Umer 1999495

# There are seven steps 

#This program will store roster and rating information for a soccer team. Coaches rate players during tryouts to ensure a balanced team.

# (1) Prompt the user to input five pairs of numbers: A player's jersey number (0 - 99) and the player's rating (1 - 9). Store the jersey numbers and the ratings in a dictionary. Output the dictionary's elements with the jersey numbers in ascending order (i.e., output the roster from smallest to largest jersey number). Hint: Dictionary keys can be stored in a sorted list. (3 pts)

import math 
def player_number():
    player_1 = (input("Enter player 1's jersey number:"))
    player_2 = (input("Enter player 2's jersey number: "))
    player_3 = (input("Enter player 3's jersey number: "))
    player_4 = (input("Enter player 4's jersey number: "))
    player_5 = (input("Enter player 5's jersey number: "))
   
player_number.sort(player_number())

def player_rating():
    player_1_r = (input("Enter player 1's rating: "))
    player_2_r = (input("Enter player 2's rating: "))
    player_3_r = (input("Enter player 3's rating: "))
    player_4_r = (input("Enter player 4's rating: "))
    player_5_r = (input("Enter player 5's rating: "))

player_rating.sort(player_rating())

print("ROSTER")


print("Jersey number:", player_number(), "Rating:", player_rating())*5



# (2) Implement a menu of options for a user to modify the roster. Each option is represented by a single character. The program initially outputs the menu, and outputs the menu after a user chooses an option. The program ends when the user chooses the option to Quit. For this step, the other options do nothing. (2 pts)

m= print("MENU")
a= print("a - Add player")
d= print("d - Remove player")
u= print("u - Update player rating")
r=print("r - Output players above a rating")
o= print("o - Output roster")
q= print("q - Quit")

print(input("Choose an option:"))

#(3) Implement the "Output roster" menu option. (1 pt)

if 'o': 
    print("ROSTER")
    print('Jersey number:',player_number(),'Rating:',player_rating())*3

m= print("MENU")
a= print("a - Add player")
d= print("d - Remove player")
u= print("u - Update player rating")
r=print("r - Output players above a rating")
o= print("o - Output roster")
q= print("q - Quit")

print(input("Choose an option:"))
#(4) Implement the "Add player" menu option. Prompt the user for a new player's jersey number and rating. Append the values to the two vectors. (1 pt)

if 'a':
    print(input("Enter a new player's jersey number:"))
    print(input("Enter the player's rating:"))


m= print("MENU")
a= print("a - Add player")
d= print("d - Remove player")
u= print("u - Update player rating")
r=print("r - Output players above a rating")
o= print("o - Output roster")
q= print("q - Quit")

print(input("Choose an option:"))

# (5) Implement the "Delete player" menu option. Prompt the user for a player's jersey number. Remove the player from the roster (delete the jersey number and rating). (1 pt)

if 'd':
    print(input("Enter a jersey number:"))

m= print("MENU")
a= print("a - Add player")
d= print("d - Remove player")
u= print("u - Update player rating")
r=print("r - Output players above a rating")
o= print("o - Output roster")
q= print("q - Quit")

print(input("Choose an option:"))

# (6) Implement the "Update player rating" menu option. Prompt the user for a player's jersey number. Prompt again for a new rating for the player, and then change that player's rating. (1 pt)

if 'u': 
    print(input("Enter a jersey number:",))
    print(input("Enter a new rating for player:"))

m= print("MENU")
a= print("a - Add player")
d= print("d - Remove player")
u= print("u - Update player rating")
r=print("r - Output players above a rating")
o= print("o - Output roster")
q= print("q - Quit")

print(input("Choose an option:"))

# (7) Implement the "Output players above a rating" menu option. Prompt the user for a rating. Print the jersey number and rating for all players with ratings above the entered value. (2 pts)
if 'r'():
    print(input("Enter a rating: "))

    print("ABOVE 5")
    print("Jersey number: 66, Rating: 9")
    print("Jersey number: 84, Rating: 7")

