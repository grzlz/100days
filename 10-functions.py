# Create a calculator  
import os 

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_dict = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number? "))
    for i in calculator_dict:
        print(i)

    keep_going = True
    while keep_going:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        function = calculator_dict[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
            num1 = answer

        else:
            keep_going = False
            os.system("clear")
            calculator()

calculator()

    
