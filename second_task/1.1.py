from random import choice

class Car:
    def __init__(self, speed:int, name):
        self.speed = speed
        self.name = name

class Illigal_Race:
    @staticmethod
    def Race(cars_list, laps:int):
        temp_list = [i for i in cars_list]
        result, count_temp = [], len(temp_list)
        if laps > count_temp:
            laps = count_temp 
        for i in range(laps):
            retired = temp_list.pop(choice(range(count_temp - i)))
            print(f"К сожалению, на {i+1} круге в аварию попал", retired.name)
            result.append(retired)
        sorted_temp_list = sorted(temp_list, key = lambda x: x.speed)
        result.extend(sorted_temp_list)
        return result[::-1]

car1 = Car(10, 'Verstappen')
car2 = Car(9, 'Hamilton')
car3 = Car(8, 'Bottas')
car4 = Car(7, 'Ocon')
car5 = Car(6, 'Vettel')
table_1 = [car1, car2, car4, car5, car3]
result_table = [i.name for i in Illigal_Race.Race(table_1, 2)]
for i in range(len(table_1)):
    print(f'{i + 1} место занял - {result_table[i]}')