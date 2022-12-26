# Check if height > 120 and age > 18. If > 18, pay 12, 12-17, pay 7, < 12 5

height = int(input("Introduce height: "))


if height > 120:
    
    age = int(input("Introduce age: "))
    photo = input("Do you want a photo? (y/n)\n")
    if age < 12:
        cost = 5
    elif age <= 18:
        cost = 7
    else: 
        cost = 12
    
    if photo == "y":
        cost += 2

    print(f"Please pay ${cost}.")
else:
    print("No ride for you :/")