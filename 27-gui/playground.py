# Create a function that adds any number of given inputs

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(2, 3, 1))

def calculate(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(argumento1=1, brgumento2=2)