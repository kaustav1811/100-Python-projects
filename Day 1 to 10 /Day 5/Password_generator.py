import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Python Random Password Generator!!")
l = int(input("How many letters you want in password:- "))
n = int(input("How many numbers you want in password:- "))
s = int(input("How many symbols you want in password:- "))

"""
#Easy level
password = ""
for i in range(0,l):
    password = password + random.choice(letters)
for i in range(0,s):
    password = password + random.choice(symbols)
for i in range(0,n):
    password = password + random.choice(numbers)
print(f"Here is your password:- {password}")
"""

#hard level - we use list instead of string
#we can also use random.shuffle(x) and pass the list, and then convert it into a string by using for loop
password_list = []
for i in range(0,l):
    password_list.append(random.choice(letters))
for i in range(0,s):
    password_list.append(random.choice(symbols))
for i in range(0,n):
    password_list.append(random.choice(numbers))
password = ""
for i in range(0,len(password_list)):
    password = password + random.choice(password_list)
print(f"Here is your password:- {password}")