from long_file import MENU, resources

user_input = input("What do you want to have? You can pick a espresso, a latte or a cappuccino:\n")

if user_input == "report":
    for key in resources:
        print(f"{key.capitalize()}: {resources[key]}")

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
        print(i, resources[i])
    print(f"Here is yout {beverage}!")
    
make_beverage(user_input)


print(check_resources(user_input))

# Create payment with coins function

#deposit = 0

#penny = float(input("How many pennies are you introducing? "))/100
#nickel = float(input("How many nickels are you introducing?"))/20
#dime = float(input("How many dimes are you introducing? "))/10
#quarter = float(input("How many quarters are you introducing? "))/4

# deposit = penny + nickel + dime + quarter

# print(deposit)

