# Create a password generator 

from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

input_pwd_length = 4
pwd = ''

for pwd_length in range(1, input_pwd_length + 1):
    random_number_for_character_type = randint(1, 3)

    if random_number_for_character_type == 1:
        # Select a random letter for next character in string 

        random_number_for_letter = randint(1, len(letters))

        pwd += letters[random_number_for_letter]

    if random_number_for_character_type == 2:

        random_number_for_number = randint(1, len(numbers))

        pwd += numbers[random_number_for_number]

    if random_number_for_character_type == 3:

        random_number_for_symbol = randint(1, len(symbols))

        pwd += symbols[random_number_for_symbol]



print(pwd)