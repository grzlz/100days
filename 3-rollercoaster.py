# Check if number is odd or even
print("Welcome to eveness number calculator!")

number = int(input("Introduce a number. (Must be integer) "))

residual = number % 2

if residual == 0:
    print("The number is even.")
else:
    print("The number is odd.")