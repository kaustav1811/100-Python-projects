#ROCK PAPER SCISSORS GAME
def rock():
    print('''
            _______
        ---'   ____)
              (_____)
              (_____)
             (____)
        ---.__(___)
    ''')

def paper():
    print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')

def scissors():
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')

import random
print("This is a Rock, Paper and Scissors game!\nWhat do you choose?")
user_choice = input("Type R for Rock,P for Paper and S for Scissors:- ")
computer_choice = random.choice(["R","P","S"])

print("Your choice:- ",end = "")
if user_choice == "P":
    paper()
elif user_choice == "R":
    rock()
else:
    scissors()

print("Computer's choice:- ",end = "")
if computer_choice == "P":
    paper()
elif computer_choice == "R":
    rock()
else:
    scissors()

if user_choice == computer_choice:
    print("Game Tied!!")
elif (user_choice == "P" and computer_choice == "R") or (user_choice == "R" and computer_choice == "S") or (user_choice == "S" and computer_choice == "P"):
    print("You Win!!")
else:
    print("You Lose!!")