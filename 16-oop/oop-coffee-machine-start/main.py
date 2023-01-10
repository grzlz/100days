from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

# Display options
# Get a valid user  and save it to a variable named drink
valid_drink = False
while valid_drink is False:
    user_input = input(f"What yould you like? Options are {menu.get_items()}:\n")
    beverage = menu.find_drink(user_input)
    if beverage:
        valid_drink = True

# Verify if machine has enough resources to make drink



# If we have enough resources, process payment
if machine.is_resource_sufficient(beverage):
    if money.make_payment(beverage.cost):
        machine.make_coffee(beverage)

        



