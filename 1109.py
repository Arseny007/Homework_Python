import string
import random

list_=[]

def rnd_string (n):
    a = ''
    for i in range(n):
        a += random.choice(string.ascii_letters)
    return a

def char_count(n):
    length_ = len(n)
    count_up = 0
    count_down = 0
    for i in range(length_):
        if n[i] in string.ascii_lowercase:
            count_up += 1
        else:
            count_down += 1
    if count_up == count_down:
        return -1
    elif count_up > count_down:
        return 1
    else:
        return 0

def mass(n,k):
    masss = []
    for i in range(k):
        b = rnd_string(n)
        masss.append(b)
    return masss

def procent(mas, n):
    count_mass = len(mass(n,k))
    ko = 0
    for i in range(count_mass):
        if char_count(mass(n, k)[i]) == 1:
            ko += 1
    return (ko/count_mass*100)


print('Введите количество символов в строке')
n = int(input())
print('Введите количество строк')
k = int(input())

massiv_strings = (mass(n,k))
print(massiv_strings)
print('Количество строк с бОльшим количеством букв в верхнем регистре = ', procent(massiv_strings, n), '%', sep='')