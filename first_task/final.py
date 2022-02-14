def solution(data, align, place, sym = ' '):
    if place < 0:
        return 'Ошибка! Выделенное место под текст должно быть положительным!'
    if align.lower() not in ['center', 'right', 'left']:
        return 'Ошибка! Выравнивание осуществляется по ключевым словам "center", "left" и "right"!'
    result, count_ = '', len(data)
    if count_ == 0:
        return 'Ошибка! На обработку подан пустой список!'
    align_sym = ['^', '<', '>'][['center', 'left', 'right'].index(align.lower())]
    for i in range(count_):
        result += '{0:{1}{2}{3}}'.format(data[i], sym, align_sym, place)
        if count_ - 1 != i:
            result += '\n'
    return result

input_flag = (input('Желаете вручную ввести значения? y/n: ').lower() == 'y')
while input_flag:
    input_data = input('Введите через пробел значения: ').split()
    input_align = input('Введите слово для центрирования: ')
    input_place = int(input('Введите место на 1 строке: '))
    input_sym = input('Введите символ заполнения (если пропущено, то символ = " "): ')
    if input_sym == '':
        input_sym = ' '
    print(solution(input_data, input_align, input_place, input_sym))
    input_flag = (input('Желаете ещё раз вручную ввести значения? y/n: ').lower() == 'y')

test_flag = (input('Запустить мои тест кейсы? y/n: ').lower == 'y')
if test_flag:
    print('my test cases')
    data_empty = []
    print(solution(data_empty, 'Center', 9))
    data = ['0', '1', '2']
    print(solution(data, 'bright', 9, '!'))
    print(solution(data, 'right', 1, '$'))
    print(solution(data, 'center', 20, '*'))
    print(solution(data, 'center', 3))
    print(solution(data, 'left', -2, '%'))