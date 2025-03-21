#To find ASCII art go here https://ascii.co.uk/art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find teh treausre!\n")

direction = input("You\'re At a CrossRoad where do you want to go Left or Right? Enter L for left and R for right ")
if direction == "R":
    print("You fell in a whole Game over YOU LOSE!")
elif direction == "L":
    decision = input("You have come to a lake.\nThere is an island in the middle of the lake. Do you want to Swim or Wait? Type S for swim and W for wait ")
    if decision == "S":
        print("You got attacked by an angry trout! Game over YOU LOSE!")
    elif decision == "W":
        door = input("You arrive at the island unharmed.\nThere is a house with three doors.\nOne red, one Yellow, One Blue.\nWhich door do you choose:- Red(R),Yellow(Y) or Blue(B) ")
        if door == "R":
            print("It's a room full of fire.\nGame over YOU LOSE!")
        elif door == "B":
            print("You enter a room of beats.\nGame over YOU LOSE!")
        else:
            print("CONGRATULATIONS YOU FOUND THE TREASURE!\nYOU WIN!!!")
    else:
        print("invalid input")
else:
    print("invalid input")