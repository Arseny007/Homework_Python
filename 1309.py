from random import randint

def palindrom(word):
    length = len(word)
    for i in range(length):
        if word[i] == word[-i-1]:
            print(word, 'является палиндромом')
            return True
        else:
            print(word, 'не является палиндромом')
            return False

def extension(name_file):
    file_list = name_file.rsplit('.')
    return file_list[-1]

def ntonnn(n):
    answer = n*10**len(str(n)) + n + n*10**(len(str(n))+len(str(n))) + n*10**(len(str(n))) + n + n
    return answer

def sec_to_time(second):
    days = second // 86400
    hours = (second - days*86400) // 3600 % 24
    minuts = (second - days*86400 - hours*3600) // 60 % 60
    seconds = second % 60
    return str(days) + ':' + str(hours) + ':' + str(minuts) + ':' + str(seconds)

def sort_1(list):
    list.sort()
    return list

def sort_2(a):
    length = len(a)
    for i in range(length-1):
        for j in range(length-i-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a


def create_list(n):
    list_ = []
    for i in range(n):
        list_.append(randint(0,99))
    return list_

print('введите количество элементов')
num = int(input())
list_random = create_list(num)
print(sort_2(list_random))

print('введите слово для проверки на палиндром')      #1111
word = input()
print(palindrom(word))

print('введите название файла')                       #2222
name = input()
print('.', extension(name), sep = '')     
           
print('введите количество секунд')                    #3333
second = int(input())
print (sec_to_time(second))

print('Напишите число для размножения')               #4444
num = int(input())
print(ntonnn(num))



    