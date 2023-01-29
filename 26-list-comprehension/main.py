import pandas as pd
# NATO exercise

d = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in d.iterrows()}


answer = []
while not answer:
    word = input("What word do you wish to NATOfy? ").upper()
    try:
        answer = [nato_dict[i] for i in word]
    except KeyError as message:
        print(f"Sorry, only letters. Key {message} does not exist.")
    else:
        print(answer)
