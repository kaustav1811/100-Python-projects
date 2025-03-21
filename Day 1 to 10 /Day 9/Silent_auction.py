import os
from art import logo
print(logo)
print("Welcome to the secret auction program")
bids = {}
decision = "yes"
while(decision == "yes"):
    name = input("What's your name:- ")
    bid = int(input("What's your bid:- $"))
    decision = input("Are there any other bidders? Type 'yes' or 'no':- ")
    bids[name] = bid
    os.system('cls')
max = int(0)
winner = ""
for name in bids:
    value = bids[name]
    if value>max:
        max = value
        winner = name
print(f"The winner is {winner} with a bid of ${max}.")