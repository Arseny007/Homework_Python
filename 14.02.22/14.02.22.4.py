class A:
    def shout(self):
        print('Whats your name')

    def say(self):
        print("I'm am obj A")

class B:
    def yell(self):
        print('Gauda')
    
    def say(self):
        print("I'm obj B")

class C(A, B):
    pass

C.shout()
C.yell()
C.say()