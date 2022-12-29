from sys import exit

# Treasure island hunt

print("Welcome to Python Treasure Island! Your mission is to find the reasure.")

direction = input("You land in a desert island. You have to choose which direction to go. Left or right? (l/r).\n")

if direction == "l":
    exit("You fell into a cliff and died. Game over.")

print("You arrived to a river. You can see an old tree crossing it and cave by the other end of it.")
river = input("Do you swim or try to cross the tree? (s/c)\n")

if  river == "s":
    exit("The current is too strong, you end up fallin from a waterfall to your death. Game over.")

print("In the cave you see three doors. The first one is blue, the second red and the third is yellow. Choose one (b/r/y).")

door = input("Choose a door. (b/r/y)\n")

if door == "b":
    print("You found the treasure!")
else:
    exit("Game over.")