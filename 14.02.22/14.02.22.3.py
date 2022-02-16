class Person:
    def __init__(self, age, name, country):
        self.age = age
        self.name = name
        self.country = country

    def say(self):
        print(f"My name is {self.name}. I'm {self.age} y.o. and I from {self.country}")

class Student(Person):
    def __init__(self, age, name, country, study):
        super().__init__(age, name, country)
        self.study = study

person_1 = Person(18, 'Ivan', 'Russia')
print(person_1.age)
person_1.say()