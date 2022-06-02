class Stack:
    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def remove(self):
        return self.stack.pop()

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)
    
    def remove(self):
        return self.queue.pop(0)

class Deck:
    def __init__(self):
        self.deck = []

    def add(self, item, end=True):
        if end:
            self.deck.append(item)
        else:
            self.deck.insert(0, item)

    def remove(self, end=True):
        return self.deck.pop() if end else self.deck.pop(0)

stack = Stack()
for i in range(5):
    stack.add(i)
print('stack before: ', *stack.stack)
print('Removed: ', stack.remove())
print('stack: ', *stack.stack)

queue = Queue()
for i in range(5):
    queue.add(i)
print('Queue before: ', *queue.queue)
print('Removed: ', queue.remove())
print('Queue: ', *queue.queue)

deck = Deck()
for i in range(3):
    deck.add(i)
print(deck.deck)

for i in range(3, 6):
    deck.add(i, False)
print(deck.deck)

print('Removed from deck: ', deck.remove())
print('After removal: ', deck.deck)
print('Removed from start: ', deck.remove(False))
print('After removal: ', deck.deck)
