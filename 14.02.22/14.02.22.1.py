# селф указывает на сам объект. везде где мы пишем селф это значит что мы будем работать с самим объектом класса
#
#
class Bakery:
    milk = 0,5
    def __init__(self, eggs, flour):
        self.eggs = eggs
        self.flour = flour

    def bake(self, temp, time):
        # self.sugar = 10   - выдаст ошибку
        pass

class Cookie(Bakery):
    def __init__(self, eggs, flour, cinramon):
        super().__init__(eggs, flour)
        self.cinramon = cinramon
    
    def __del__(self):
        super().__del__()
        print(self)
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
