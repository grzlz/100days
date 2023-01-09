# Mke guessing game
from random import randint 
from os import system
from sys import exit

logo = """
 __ _  _  _  _  _  ____  ____  ____     ___   __   _  _  ____  _   
(  ( \/ )( \( \/ )(  _ \(  __)(  _ \   / __) / _\ ( \/ )(  __)/ \  
/    /) \/ (/ \/ \ ) _ ( ) _)  )   /  ( (_ \/    \/ \/ \ ) _) \_/  
\_)__)\____/\_)(_/(____/(____)(__\_)   \___/\_/\_/\_)(_/(____)(_)                       
"""


print(f"{logo}\nWelcome to the Number Guessing Game.\nI'm thinking of a random number between 1 and 100.")

valid_option = False
while valid_option is not True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    lives = 0
    if difficulty == "easy":
        lives = 10
        valid_option = True
    elif difficulty == "hard":
        lives = 5
        valid_option = True
    else:
        system("clear")
        print("Please select a valid option.")


secret_number = randint(1, 100)

right_guess = False
print(f"You have {lives} lives to guess the secret number.")
while lives > 0 and right_guess is not True:
    guessed_number = int(input("Take a guess: "))
    
    if guessed_number > secret_number:
        lives -= 1
        print(f"Too high! Remaining lives: {lives}.")

    elif guessed_number < secret_number:
        lives -= 1
        print(f"Too low! Remaining lives: {lives}.")

    else:
        print(f"You guessed correctly! The number is {secret_number}!")
        right_guess = True

