import pandas as pd
# NATO exercise

d = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in d.iterrows()}

word = input("What word do you wish to NATOfy? ")
answer = [nato_dict.get(i.upper()) for i in word]
print(answer)