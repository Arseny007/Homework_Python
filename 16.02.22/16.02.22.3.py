class Person:
    def __init__(self, age, name, country):
        self.age = age
        self.name = name
        self.country = country

    def say(self):
        print(f"My name is {self.name}. I'm {self.age} y.o. and I from {self.country}")

class Student(Person):
    def __init__(self, age, name, country, study, num_parent):
        super().__init__(age, name, country)
        self.study = study
        self.__num_parent = num_parent

    def get_num(self):
        return self.__num_parent
    
    def set_num(self, new_num):
        self.__num_parent = new_num

student1 = Student(19, 'Name', 'Country', 'Study', '+79876543210')
print(student1.get_num())
student1.set_num('+71231231212')
print(student1.get_num())
# print(student1.__num_parent)          выводит ошибку
print(student1._Student__num_parent)