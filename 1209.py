from random import randint

def sort_1(list):
    list.sort()
    return list

def sort_2(a):
    length = len(a)
    g = 0
    bubble = 0
    while g < length - 1:
        g = 0
        for i in range(length-1):
            if a[i] > a[i+1]:
                bubble = a[i]
                a[i] = a[i+1]
                a[i+1] = bubble
        for i in range(length-1):
            if a[i] <= a[i+1]:
                g += 1
    return a


def create_list(n):
    list_ = []
    for i in range(n):
        list_.append(randint(0,99))
    return list_

print('введите количество элементов')
num = int(input())
list_random = create_list(num)
print(list_random)
print('сортировка без sort()')
print(sort_2(list_random))
print('сортировка с sort()')
print(sort_1(list_random))