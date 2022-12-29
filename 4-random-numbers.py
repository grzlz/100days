import random 

# Rock paper scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

selection = int(input("0 for Rock, 1 for Paper, 2 for Scissors.\n"))

computer = random.randint(0, 2)

options = [rock, paper, scissors]

print(f"You chose:\n{options[selection]}\nComputer chose:\n{options[computer]}")

if selection == computer:
    print("It's a draw")

elif selection == 0 and computer == 1:
    print("You lose")

elif selection == 0 and computer == 2:
    print("You won!")

elif selection == 1 and computer == 0:
    print("You won!")

elif selection == 1 and computer == 2:
    print("You lost!")

elif selection == 2 and computer == 1:
    print("You won!")

else:
    print("You lost!")



1