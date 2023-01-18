#TODO: Create a letter using starting_letter.txt 

text_list = ["Hola", "que hace", "perro"]

with open("./Input/Names/invited_names.txt") as file:
    guests = file.readlines()
    guests = [guest.strip() for guest in guests]

with open("./Input/Letters/starting_letter.txt", mode="r") as template:
    template_letter = template.read()

for guest in guests:
    with open(f"./Output/ReadyToSend/letter_to_{guest}.txt", mode="w") as file:
        modified_letter = template_letter.replace("[name]", guest)
        file.write(modified_letter)
