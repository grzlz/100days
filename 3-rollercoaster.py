# Check if height > 120 and age > 18. If > 18, pay 12, 12-17, pay 7, < 12 5

height = int(input("Introduce height: "))


if height > 120:
    age = int(input("Introduce age: "))
    if age >= 18:
        print("Pay 12.")
    elif age < 18 and age >= 12:
        print("Pay $7.")
    else: 
        print("Pay $5.")
else:
    print("No ride for you :/")