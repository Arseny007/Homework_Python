from random import randint

def create_list(n):
    list_ = []
    for i in range(n):
        list_.append(randint(0,9))
    return list_

def unique(list_):
    unique_set = set(list_)
    uniq_list = list(unique_set)
    return uniq_list

def intersection_of_sets(set1, set2):
    is_ = set.intersection(set1, set2)
    return is_
    

print('введите количество элементов в списке:')
n = int(input())
rnd_list1 = create_list(n)
rnd_list2 = create_list(n)
print(rnd_list1)
print(rnd_list2)
print('уникальные элементы списков:')
print(unique(rnd_list1))
print(unique(rnd_list2))
print('пересечение:')
print(list(intersection_of_sets(set(rnd_list1), set(rnd_list2))))