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

# Benefits of using .get on dictonaries and optional keywords

class Car:
    def __init__(self, **kwargs):
        self.maker = kwargs.get("maker")
        self.model = kwargs.get("model")

my_car = Car(maker="Nissan")
print(my_car.maker)
# This prints None, if I had used kwargs["model"] if would return an error.