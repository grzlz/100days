# Create animal class and fish class

class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

    def swim(self):
        print("Moving in water.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("But underwater.")


fish = Fish()
fish.swim()
fish.breathe()  