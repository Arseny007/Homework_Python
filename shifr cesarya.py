rus_alp = [i for i in 'абвгдежзийклмнопрстуфхцчшщъыьэюя']
rus_alp_up = [i.upper() for i in rus_alp]
eng_alp = [chr(i) for i in range(ord('a'), ord('z')+1)]
eng_alp_up = [chr(i) for i in range(ord('A'), ord('Z')+1)]

def shifrator(text, step, temp):
    result = ''
    for i in range(len(text)):
        if text[i].lower() not in temp:
            result += text[i]
        else:
            if text[i].islower():
                result += temp[(len(temp) + temp.index(text[i])+step) % len(temp)]
            else:
                result += temp[(len(temp) + temp.index(text[i].lower())+step) % len(temp)].upper()
    return result

def shifr():
    print('Введите текст:')
    text = input()
    if text[0].lower() in rus_alp:
        temp = rus_alp
    else:
        temp = eng_alp
    step = input('Введите шаг для шифра или "да" для вывода шифрации всех шагов или "дада" для сдвига в зависимости от длины слова: ')
    if step.lower() == 'да':
        result = [shifrator(text, step, temp) for step in range(1, len(temp))]
    elif step.lower() == 'дада':
        text = text.split()
        for i in range(len(text)):
            result = [shifrator(text[i], len(text[i].strip('!@#$%^&*()_+-="№;:?,.<>"')), temp)]
    elif (input('"ш" = шифровать, "д" = дешифровать: ').lower() == 'д'):
        step = -step
        result = []
        result.append(shifrator(text, step, temp))
    return result

   
def main():
    print('Добро пожаловать в шифратор\дешифратор Цезаря.')
    again = True
    while again:
        result = shifr()
        if len(result) == 31:
            print(', '.join(result[0:7]), ', '.join(result[8:15]), ', '.join(result[16:23]), ', '.join(result[24:31]), sep=',\n')
        else:
            print(result, sep='')
        again = (input('Перезапустить де\шифратор? "д" = да: ')[0].lower() == 'д')
    return None

main()