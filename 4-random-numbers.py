import random 

# Banker roulette
names = input("Introduce the names of the involved bankers separated by a comma.\n")

names_list = names.split(", ")

list_length = len(names_list) - 1

choose_index = random.randint(0, list_length)

print(f"{names_list[choose_index]} will pay the bill.a,")