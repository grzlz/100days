# Prime number checker

input_number = int(input("Introduce a number: "))

def prime_number(input_number):
    for number in range(2, input_number):
        if input_number % number == 0:
            return(print("Not a prime number."))
        else: 
            return(print("It is a primer number!"))
    
prime_number(input_number)