print("Welcome to python Pizza Deliveries!")
size = input("Which size pizza do u need? S,M or L: ")
total_bill = 0
if size=="S":
    total_bill += 15
    peppreroni = input("Add peppreroni? Type:- Y for yes or N for no ")
    if peppreroni == "Y":
        total_bill += 2
elif size=="M":
    total_bill += 20
    peppreroni = input("Add peppreroni? Type:- Y for yes or N for no ")
    if peppreroni == "Y":
        total_bill += 3
else:
    total_bill += 25
    peppreroni = input("Add peppreroni? Type:- Y for yes or N for no ")
    if peppreroni == "Y":
        total_bill += 3
extra_cheese = input("Do you want extra cheese? ")
if extra_cheese == "Y":
    total_bill += 1

print(f"The total bill for your pizza is:- ${total_bill}")