# You are painting a wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# A can of pain and cover 5sqm.
# Round up the result

def get_cans(height, width):
    sqm = height * width
    number_of_cans = round(sqm / 5)

    return number_of_cans

height = int(input("Introduce Height: "))
width = int(input("Introduce Width: "))

print(f"Yoy should get {get_cans(height, width)} cans.")