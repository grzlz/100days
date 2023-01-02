from random import choice

word_list = ["ardvark", "baboon", "camel"]

chosen_word = choice(word_list)






display = []
for i in chosen_word:
    display.append("_")

# Use a while loop to let the user guess again until there are no more "_" to display.
while "_" in display:
    guessed_letter = input("Guess a letter.\n")
    guessed_letter = guessed_letter.lower()

    for i in range(len(chosen_word)):

        if guessed_letter == chosen_word[i]:
            display[i] = guessed_letter
            print(display)
        


if "_" not in display:
    print("You won!")   
