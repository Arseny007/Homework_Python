words = ['Загаданное число больше. попробуй ещё, В следующий раз обязательно повезет!', 
        'Поздравляю! Ты угадал число',
        'Загаданное число меньше. попробуй ещё, в следующий раз обязательно повезет!']

from random import *

print('Добро пожаловать в числовую угадайку')

def is_valid(n, rang_e):
    return (int(n) in range(1, rang_e+1)) and (n.isdigit())

def comparison(hid_num_in_str, ent_num):
    hid_num = int(hid_num_in_str)
    if hid_num == ent_num:
        return 1
    elif hid_num < ent_num:
        return 0
    elif hid_num > ent_num:
        return 2

def mein_func(true_num, hid_num, hid_range, counter):
    if is_valid(true_num, hid_range):
        print(words[comparison(true_num, hid_num)])
        if comparison(true_num, hid_num) != 1:
            next_num = input()
            mein_func(next_num, hid_num, hid_range, counter + 1)
    else:
        print(f'Может быть все-таки целое число от 1 до {hid_range}')
        next_num = input()
        mein_func(next_num, hid_num, hid_range, counter + 1)
    if comparison(true_num, hid_num) == 1:
        global attempts 
        attempts = counter
    

def game():
    print('Введите конец диапазона для загадывания числа, если значение пустое, то диапазон [1, 100]')
    hid_range = input()
    if hid_range == '':
        hid_range = 100
        hid_num = randint(1, hid_range)
    else:
        hid_num = randint(1, int(hid_range))
    print(f'Введите целое число в диапазоне от 1 до {hid_range}, попробуйте угадать загаданное число')
    ent_num = input()
    mein_func(ent_num, hid_num, int(hid_range), 1)
    print(f'Ты справился с {attempts} попытки!')
    print('Чтобы начать заново, введите "1"', 'Чтобы закончить, введите "0"', sep='\n')
    answer = input()
    if answer == '1':
        game()
    elif answer == '0':
        return None

game()