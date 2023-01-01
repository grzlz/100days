from random import choice

word_list = ["ardvark", "baboon", "camel"]

chosen_word = choice(word_list)

guessed_letter = input("Guess a letter.\n")
guessed_letter = guessed_letter.lower()




display = []
for i in chosen_word:
    display.append("_")

for i in range(len(chosen_word)):

    if guessed_letter == chosen_word[i]:
        
        display[i] = guessed_letter
    

print(display)

