from word_list import different_words
from art import hangman
from art import logo
placeholder = ""
lives = 6
correct_letters = []
game_over = False

print(logo)

import random
choosen_word = random.choice(different_words)
for l in choosen_word:
    placeholder =  placeholder + "_" + " "
placeholder = placeholder.rstrip()
print(f"The word choosen by the compiler is {placeholder}")
while not game_over and lives>0:
    guess = input("Guess a letter:- ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}.")
    display = ""
    if guess in choosen_word:
        print("Letter present")
        for letter in choosen_word:
            if letter == guess:
                display += guess + " "
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter + " "
            else:
                display += "_" + " "
        print(display.rstrip())
        hangman(lives)
        if '_' not in display:
            game_over = True
            print(f"The word is {choosen_word.upper()}, You win!")
    else:
        print("Letter not present.You Lose a life.")
        lives -= 1
        hangman(lives)
if lives == 0:
    print("YOU LOSE!! You are out of lives, Better luck next time.")
    print(f"The word was:- {choosen_word}.")