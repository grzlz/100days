# Prime number checker

input_number = int(input("Introduce a number: "))

def prime_number(input_number):
    found_prime = True
    for number in range(2, input_number):
        if input_number % number == 0:
            found_prime = False


    if found_prime:
        print("It's a prime number!")

    else:
        print("It's not a prime number.")


prime_number(input_number)