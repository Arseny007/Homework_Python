def solution(data, align, sym, place):
    if place < 0:
        return 'Ошибка! Выделенное место под текст должно быть положительным'
    align_sym = ['^', '<', '>'][['center', 'left', 'right'].index(align)]
    result, count_ = '', len(data)
    for i in range(count_):
        result += '{0:{3}{1}{2}}'.format(data[i], align_sym, place, sym)
        if count_ - 1 != i:
            result += '\n'
    return result

data = ['0', '1', '2', '3', '4']
print(solution(data, 'right', '!', 9))
print(solution(data, 'right', '$', 1))
print(solution(data, 'center', '*', 20))
print(solution(data, 'center', ' ', 3))
print(solution(data, 'left', '%', -2))