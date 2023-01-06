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

operation_symbol = input("Pick an operation from the linea above: ")

num2 = int(input("What's the second number?: "))



function = calculator_dict[operation_symbol]
answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

keep_going = True
while keep_going:
    old_answer = answer

    if input(f"Type 'y' to continue calculating with {old_answer} or type 'n' to exit: ") == "n":
        break

    new_symbol = input("Pick an operation: ")    
    new_number = int(input("What's the next number? "))
    
    function = calculator_dict[new_symbol]
    answer = function(new_number, answer)

    print(f"{old_answer} {new_symbol} {new_number} = {answer}")

    
