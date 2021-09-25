import random

def gen(n):
    for i in range(n):
        yield gen_names()

def gen_names():
    name = ''
    name = chr(random.randint(65, 90))
    rnd_num = random.randint(3, 10)
    for u in range(rnd_num):
        name += chr(random.randint(97, 122))
    return name

print('введите количество имён:')
n = int(input())
a = gen(n)
for b in a:
    print(b)