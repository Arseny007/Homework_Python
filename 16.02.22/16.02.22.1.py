class ExQuote:
    def __init__(self, quote):
        self.quote = quote
    
    def say(self):
        return self.quote + '1'

class QQuote:
    def __init__(self, quote):
        self.quote = quote
    
    def say(self):
        return self.quote + '2'

a = ExQuote('blablabla')
b = QQuote('tyuio')
print(a.say())
print(b.say())