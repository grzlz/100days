from long_file import data
from random import choice 
from os import system as sys

# Greet
print("Welcome to Higher or Lower!")

# Create a function to select randomly an element from data list

def random_account():
    return choice(data)

# Create score variable = 0
score = 0

# Display text showing information about the account owner.

keep_playing = 'y'
while keep_playing == 'y':
    game_over = False

    first_account = random_account()
    next_account = random_account()

    while game_over is not True:
        print(f"Who has more followers on Instagram? {first_account['name']}, {first_account['description']} from {first_account['country']} or {next_account['name']}, {next_account['description']} from {next_account['country']}?: ")

        answer = input(f"Type 'A' for {first_account['name']} or 'B' for {next_account['name']}: ")

        if answer == "A":
            if first_account['follower_count'] >= next_account['follower_count']:
                next_account = random_account()
                score += 1
                print("Correct!")
                sys("clear")
            else:
                print(f"Wrong! {next_account['name']} has {next_account['follower_count']} while {first_account['name']} has {first_account['follower_count']}.\nYour score was: {score}.")
                game_over = True

        elif answer == "B":
            if first_account['follower_count'] < next_account['follower_count']:
                first_account = next_account
                next_account = random_account()
                score += 1
                print("Correct!")
                sys("clear")
            else:
                print(f"Wrong! {first_account['name']} has {first_account['follower_count']} while {next_account['name']} has {next_account['follower_count']}.\nYour score was: {score}.")            
                game_over = True

    keep_playing = input("Play again? Type 'y' or 'n': ")
    if keep_playing == "n":
        print("Bye!")
    sys("clear")
    