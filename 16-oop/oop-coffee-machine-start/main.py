from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

# Display options
# Get a valid user  and save it to a variable named drink
is_on = True
valid_drink = False

while is_on:
    user_input = input(f"What yould you like? Options are {menu.get_items()}:\n")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        machine.report()
        money.report()
    else:
        beverage = menu.find_drink(user_input)
        if beverage:
            if machine.is_resource_sufficient(beverage):
                if money.make_payment(beverage.cost):
                    machine.make_coffee(beverage)
