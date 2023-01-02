from random import choice


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = choice(word_list)


# Create a variable called 'lives' to keep track of the number of lifes left. Set lives equal to 6

lives = 6

# If guess is not a letter in chosen word, then reduce lives by 1. If lifes goes down to 0 then the game should stop and print 'You lose'.
display = []
for i in chosen_word:
    display.append("_")

# Use a while loop to let the user guess again until there are no more "_" to display.
while "_" in display:
    guessed_letter = input("Guess a letter.\n")
    guessed_letter = guessed_letter.lower()

    if guessed_letter not in chosen_word:
        lives -= 1
        

    for i in range(len(chosen_word)):

        if guessed_letter == chosen_word[i]:
            display[i] = guessed_letter

    print(stages[lives])
    print(display)

    if lives == 0:
        print("You lose!")
        break

    if "_" not in display:
        print("You won!")   
        break
