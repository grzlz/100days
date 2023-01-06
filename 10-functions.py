# Create a calculator  

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

num1 = int(input("What's the first number? "))
for i in calculator_dict:
    print(i)

keep_going = True
while keep_going:

    operation_symbol = input("Pick an operation from the linea above: ")

    num2 = int(input("What's the next number?: "))

    function = calculator_dict[operation_symbol]
    answer = function(num1, num2)



    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
        num1 = answer

    else:
        keep_going = False

    
