from art import logo
print(logo)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser():
    restart = "yes"

    while(restart == "yes"):
        direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
        message = input("Type the message:- ").lower()
        shift = int(input("Type the shift number:- "))
        if direction == "decode":
            shift *= -1
        encrypted_message = ""
        for letter in message:
            if letter in alphabets:
                index = alphabets.index(letter)
                encrypted_message += alphabets[(index+shift)%26]
            else:
                encrypted_message += letter
        if direction == "encode":
            print(f"The encoded message is:- \"{encrypted_message}\".")
        else:
            print(f"The decoded message is:- \"{encrypted_message}\".")
        restart = input("Do you want to encode/decode again? Type 'yes' or 'no':- ").lower()
        if restart != "yes":
            print("GoodBye!")

caeser()