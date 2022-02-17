class Washing:
    def __init__(self, water):
        self.water = water

    def wash(self, item):
        print(f"I'm washing {item} with {self.water} l of water")

class Driving:
    @staticmethod
    def drive(a, b):
        print(f"Я везу из {a} в {b}")

class Machine:
    def __init__(self, brand, price, year, color):
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color

class Washing_Machine(Washing, Machine):
    def __init__(self, water, brand, price, year, color):
        Washing.__init__(self, water)
        Machine.__init__(self, brand, price, year, color)
    

class Driving_Machine(Driving, Machine):
    def driving_machine():
        pass

car_1 = Driving_Machine
car_1.drive('gag', 'aga')
car_1.price = 300
print(car_1.price)
wash_b = Washing_Machine(5, 'ferrari', 500, 2019, 'red')
wash_b.wash('item')