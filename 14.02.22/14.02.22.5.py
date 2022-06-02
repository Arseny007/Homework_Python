from traceback import print_exception


class Washing:
    def __init__(self, water):
        self.water = water

    def wash(self, item):
        print(f"I'm washing {item} with {self.water} l of water")

class Driving:
    def drive(a, b):
        print(f"Я везу из {a} в {b}")

class Machine:
    def __init__(self, brand, price, year, color):
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color

class Driving_Mashing():
    pass