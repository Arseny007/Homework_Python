# ДЗ - написать функцию, которая принимает список аргументов
# выравнивание ('center', 'left', 'right')
# символ заполнения
# место
# например
# func([1,2,3], 'center', '*', 9)
# >>> ****1****
# ****2****
# ****3****

def final_test(data, align, sym, place):
    result = ''
    for i in range(len(data)):
        result += ''.format()

        print(1)
    return 0

def test_1(data):
    result = ''
    count_ = len(data)
    for i in range(count_):
        result += data[i]
        if count_ - 1 != i:
            result += '\n'
    return result

def test_2(data, align, sym, place):
    align_sym = ['^', '<', '>'][['center', 'left', 'right'].index(align)]
    result, count_ = '', len(data)
    for i in range(count_):
        result += '{0:{3}{1}{2}}'.format(data[i], align_sym, place, sym)
        if count_ - 1 != i:
            result += '\n'
    return result

data = ['0', '1', '2', '3', '4']
print(test_1(data))
print(test_2(data, 'right', '!', 9))
print(test_2(data, 'right', '$', 1))
print(test_2(data, 'center', '*', 20))
print(test_2(data, 'center', ' ', 3))
print(test_2(data, 'left', '%', 0))