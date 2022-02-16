class Car:
    steering_wheel = True
    def __init__(self, color, engine, wheels):
        self.color = color
        self.engine = engine
        self.wheels = wheels

    def drive(self, speed, A, B, list_of_load):
        time = (A.place - B.place)/speed
        for item in list_of_load:
            item.place = B
        return time

class Ferrari(Car):
    def __init__(self, color, engine, wheels):
        if not (engine == 'v8' or engine == 'v12'):
            print('Error')
            raise Exception
            return
        else:
            super().__init__(color, engine, wheels)
            self.manfct = 'Ferrari'

car_2 = Ferrari('red', 'v8', 4)
print(car_2.manfct, car_2.steering_wheel)
car_1 = Car('red', 'v8', 6)
print(car_1.color)
# >>> 'red'
