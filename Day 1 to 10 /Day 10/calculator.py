from art import logo1
from art import logo2

def draw():
    print(logo1)
    print(logo2)

draw()

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    decision = "yes"
    a = float(input("What's the first number:- "))
    while(decision == "yes"):
        print("+ - * /")
        symbol = input("Pick an operation:- ")
        b = float(input("What's the second number:- "))
        result = operations[symbol](a,b)
        print("")
        print(f"{a} {symbol} {b} = {result}")
        print("")
        print(f"Type 'yes' if you want to continue calculating with {result} OR")
        print("type 'no' to start a new calculation OR")
        decision = input("type 'exit' to end:- ")
        if decision == "yes":
            a = result
        elif decision == "no":
            print("\n"*20)
            draw()
            calculator()
        else:
            print("Thankyou!!")
            break

calculator()