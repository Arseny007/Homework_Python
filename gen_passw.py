from random import choice

digits = [str(i) for i in range(2, 10)]
lowercases = [i for i in 'qwertyuopasdfghjkzxcvbnm']
uppercases = [i for i in 'QWERTYUOPASDFGHJKZXCVBNM']
punc = [i for i in '!@#$%^&*()-_№;:?']
neodn = [i for i in 'il1ILo0O']
chars = [digits, lowercases, uppercases, punc, neodn]

def gen_passw(answs):
    result = [''] * int(answs[0])
    print(result)
    temp_chars = []
    for i in range(2, 7):
        if answs[i] == 'д':
            temp_chars += chars[i-2]
    for i in range(int(answs[0])):
        for j in range(int(answs[1])):
            result[i] += choice(temp_chars)
    return result


def main():
    print('Добро пожаловать в генератор паролей!')
    print('Введите в одной строке через пробел необходимое количество сгенерируемых паролей, количество букв в одном пароле, включать ли строчные буквы, заглавные, цифры, пунктуационные знаки, неоднозначные символы "il1Lo0O"', '"д" = да, "н" = нет', 'Если строка пуста то будут приняты параметры "5 10 д д д д н" ', sep='\n')
    answs = input()
    if answs == '':
        answs = '10 5 д д д д н'
    answs = answs.split()
    print(answs)
    
    return gen_passw(answs)
    
    
again = True
while again:
    print(*main())
    print('Перезапустить генератор паролей? "д" = да')
    again = (input().lower() == 'д')

