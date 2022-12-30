# Fizz buz. If number divisible by 3, print Fizz, if divisible by 5 print Buzz. If divisible by 3 and 5, print fizzbuz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuz")
    
    elif i % 3 == 0:
        print("Fizz")
    
    elif 1 % 5 == 0:
        print("Buzz")
    
    else:
        print(i)
    
