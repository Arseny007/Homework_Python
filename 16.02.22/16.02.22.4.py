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

    def __eq(self, s):
        return (self.name == s.name) and (self.age == s.age)


student1 = Student(19, 'Name', 'Country', 'Study', '+79876543210')
student2 = Student(20, 'Name', 'Country', 'Study', '+79876543210')

print(student1.__eq(student2))