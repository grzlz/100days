from sys import exit

# Treasure island hunt

print("Welcome to Python Treasure Island! Your mission is to find the reasure.")

direction = input("You land in a desert island. You have to choose which direction to go. Left or right? (l/r).\n")

if direction == "l":
    exit("You fell into a cliff and died. Game over.")

