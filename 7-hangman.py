from hangman import stages, logo
from getpass import getpass
import os 
print(logo)

chosen_word = getpass("Choose the word to guess: ").lower()


# Create a variable called 'lives' to keep track of the number of lifes left. Set lives equal to 6

lives = 6

# If guess is not a letter in chosen word, then reduce lives by 1. If lifes goes down to 0 then the game should stop and print 'You lose'.
display = []
for i in chosen_word:
    display.append("_")

# Create end of game variable equal to False, we will loop while it's true
end_of_game = False


# Use a while loop to let the user guess again until there are no more "_" to display.
while not end_of_game:
    guessed_letter = input("Guess a letter: ").lower()
    os.system('cls')

    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"'{guessed_letter}' is not in the chosen word. Try again!")
        if lives == 0:
            end_of_game = True
            print("You lose!")

    for i in range(len(chosen_word)):
        if guessed_letter == chosen_word[i]:
            display[i] = guessed_letter

    print(f"{' '.join(display)}")

    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You won!")   
