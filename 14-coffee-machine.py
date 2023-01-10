from long_file import MENU, resources
from os import system

# Create a function to check if resources are sufficient
def check_resources(beverage):
    for i in MENU[beverage]["ingredients"]:
        if resources[i] < MENU[beverage]["ingredients"][i]:
            return False
        else:
            return True

# Create function to make beverage and take the ingredients used
def make_beverage(beverage):
    for i in MENU[beverage]["ingredients"]:
        resources[i] -= MENU[beverage]["ingredients"][i]
    print(f"Here is your {beverage}. Enjoy!")
    
# Create payment with coins function
def payment(beverage):
    deposit = 0
    penny = float(input("How many pennies are you introducing? "))/100
    nickel = float(input("How many nickels are you introducing? "))/20
    dime = float(input("How many dimes are you introducing? "))/10
    quarter = float(input("How many quarters are you introducing? "))/4
    deposit = penny + nickel + dime + quarter

    if deposit > MENU[beverage]["cost"]:
        print(f"Here's your change: ${round(deposit - MENU[beverage]['cost'], 2)}.")
        resources["money"] += MENU[beverage]["cost"]
        return True
    elif deposit == MENU[beverage]["cost"]:
        resources["money"] += MENU[beverage]["cost"]
        print("You payed exactly. No change.")
        return True
    else: 
        return False

# Create flow of the program
print("Welcome to the coffe machine program!")
keep_going = True
while keep_going:
    system("clear")
    user_input = input("What do you want to have? You can pick a espresso, a latte or a cappuccino:\n")
    if user_input == "report":
        for key in resources:
            print(f"{key.capitalize()}: {resources[key]}")
    elif user_input not in [beverage for beverage in MENU]:
        print("Please enter a valid option.")
    else:
        check_resources(user_input)
        if check_resources(user_input): 
            if payment(user_input):
                make_beverage(user_input)
            else: 
                print("Not enough money.")
        else:
            print("Insufficient ingredients.")
    if input("Do you want something else? Type 'y' or 'n': ") == 'n':
        keep_going = False
        print("Bye!")