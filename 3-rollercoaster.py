# Check if height > 120 and age > 18. If > 18, pay 12, else 7

height = int(input("Introduce height. "))


if height > 120:
    age = int(input("Introduce age. "))
    if age > 18:
        print("Pay 12.")
    else:
        print("Pay $7")
else:
    print("No ride for you :/")