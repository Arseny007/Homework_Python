# n = '1234'
# # nlist = n.split()
# nlist = [i for i in n]
# print(nlist)
# n = 0
# listn = [0, 0, 0, 0, 0]
# for i in range(1729, 100000):
#     for j in range(1, 33):
#         if j**3 > i:
#             break
#         for k in range(1, 33):
#             if k**3 > i:
#                 break
#             for l in range(1, 33):
#                 if (l**3 > i) and l == j:
#                     break
#                 for h in range(1, 33):
#                     if (h**3 > i) and (h == j) and (h == k):
#                         break
#                     if (j**3 + k**3 == l**3 + h**3 == i):
#                         listn.append(i)
#                         n += 1
#                         break
#     if n > 300:
#         break
# print(listn)

# digits = input().split()
# print(digits)
# for i in range(len(digits)):
#     digits[i] = int(digits[i])
# print(digits)

# n = 'abch12345habc'
# res = ''
# h1, h2 = 0, 0
# ranger = [i for i in range(len(n))]
# for i in ranger:
#     if n[i] == 'h':
#         h1 = i
#         break
# for i in ranger:
#     if n[len(n)-i-1] == 'h':
#         h2 = i
#         break
# for i in range(len(n),h1+1):
#     res += n[i]
# for i in range(h2-1, h1, -1):
#     res += n[i]
# for i in range(h2, len(n)):
#     res += n[i]
# print(res)

# n = [i for i in range(10)]
# print(n[::-1])

# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# print(numbers)
# for i in [0, 1, 2]:
#     numbers.append(4+i)
# print(numbers)
# n = numbers.pop(0)
# print(numbers)
# numbers.extend(numbers)
# print(numbers)
# numbers.insert(3, 25)
# print(numbers)

# n = '3 3 3 3 3'
# digits = n.split()
# for i in range(len(digits)):
#     digits[i] = int(digits[i])
# count = 0
# for i in range(len(digits)):
#     for j in range(i+1, len(digits)):
#         if digits[i] == digits[j]:
#             count += 1
# print(count)

# n = [int(i) for i in input().split()]
# maxim, minim = 0, 10000
# for i in n:
#     if i < minim:
#         minim = i
#     if i > maxim:
#         maxim = i
# ind_of_max = n.index(maxim)
# ind_of_min = n.index(minim)
# n[ind_of_max] = minim
# n[ind_of_min] = maxim
# n1 = [str(i) for i in n]
# res = ' '.join(n1)
# print(res)

# n = input().split()
# print(n)

# a = [3, 4, 5, 6]
# a[2] = a.pop(0)
# print(a)

# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# n = len(a)
# ass = []
# for i in range(n):
#     minim = 100
#     for j in range(i):
#         if a[j] < minim:
#             minim = a[j]
#     ass.append(minim)
#     if minim in a:
#         a.pop(a.index(minim))

# a1 = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# print(a)
# a1.sort()
# print(a1)

# n = [1, 2, 3]
# print(sum(n))

# n = '7-137-134-5793'
# print(n[:2], len(n))

# digits = [0, 1, 2, 4, 5, 6, 8, 9, 10, 11]
# tire = [3, 7]
# n = '123-4586-3456'
# rights = 0
# if (len(n) == 14 and n[:2] == '7-') or len(n) == 12:
#     if n[:2] == '7-':
#         nnew = n[2:]
#     else:
#         nnew = n
#     for i in digits:
#         if nnew[i] in '0123456789':
#             rights += 1
#     for i in tire:
#         if nnew[i] == '-':
#             rights += 1
#     if rights == 12:
#         print('YES')
#     else:
#         print('NO', rights)
# else:
#     print('NO')

# def draw_box():
#     print('*' * 10)
#     [print('*', ' ' * 8, '*') for i in range(12)]
#     print('*' * 10)

# draw_box()

# N = [input().split() for i in range(int(input()))]
# for i in range(len(N)):
#     for j in range(len(N[i])):
#         N[i][j] = int(N[i][j])
# def quick_merge(list1, list2):
#     result = []

#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2

#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1

#     if p1 < len(list1):   # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
    
#     return result

# total = []
# for i in range(len(N)-1):
#     total = quick_merge(total, N[i])
# for i in range(len(total)):
#     total[i] = str(total[i])
# print(*total)

# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# prime_digits = []
# not_prime_digits = []
# for n in range(1, 300, 2):
#     c = 0
#     for j in range(2, n):
#         if n % j == 0:
#             c = 1
#             break
#     if c == 0:
#         prime_digits.append(n)
#     else:
#         not_prime_digits.append(n)

# for i in prime_digits:
#     if not is_prime(i):
#         print(i)
    
# for i in not_prime_digits:
#     if is_prime(i):
#         print(i)

# def is_prime(num):
#     result = True
#     for i in range(2, num):
#         if num % i == 0:
#             result = False
#     return result

# n = int(input())
# print(is_prime(n))

# def is_palindrome(text):
#     n = [i for i in text]
#     i=0
#     result = True
#     while i < len(n): 
#         if n[i] in '!"№;%:?*()-_=+@#$^&,./\| ':     # Поиск знака
#             n.pop(i)                                # Удаление знака
#         else:
#             i += 1                                  # Если символ - не знак, идем дальше. если был бы знак, удалили бы элемент и элементы списка продвинулись бы дальше сами
#     for i in range(len(n)):
#         n[i] = n[i].lower()
#     for i in range(len(n)):
#         if n[i] != n[len(n)-i-1]:
#             result = False
#     return result
        
# txt = 'Standart - smallest, sell Amstrad nats.'
# print(is_palindrome(txt))

# passw = '568:839:138'
# n = passw.split(':')
# print(n)

# def is_correct_bracket(text):
#     n = []
#     result = True
#     for i in text:
#         if i == '(':
#             n.append(')')
#         else:
#             if len(n) != 0:
#                 n.pop()
#             else:
#                 result = False
#     if len(n) != 0:
#         result = False
#     return result
        
# txt = input()
# print(is_correct_bracket(txt))

# def convert_to_python_case(text):
#     n = text[0].lower()
#     for i in range(1, len(text)):
#         if text[i].isupper():
#             n = n + '_' + text[i].lower()
#         else:
#             n += text[i]
#     return n
# txt = 'TiOfnidOnvruNdh'
# print(convert_to_python_case(txt))

# def get_middle_point(x1, y1, x2, y2):
#     return (x1 - x2)//2, (y1 - y2)//2
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# def solve(a, b, c):
#     D = b**2 - 4 * a * c
#     x2 = 0
#     x1 = (-b - (D**0.5)) / (2 * a)
#     if D == 0:
#         x2 = x1
#     else:
#         x2 = (-b + (D**0.5)) / (2 * a)
#     return min(x1, x2), max(x1, x2)
# a, b, c = int(input()), int(input()), int(input())
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# def draw_triangle():
#     for i in range(8):
#         print(' '*(7-i), '*'*(1+i*2), sep='')
# draw_triangle()4

# def compute_binom(n, k):
#     return int(fact(n)/(fact(k)*fact(n-k)))
# def fact(n):
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
#     return res
# n = int(input())
# k = int(input())
# print(compute_binom(n, k))

# def number_to_words(num):
#     res = ''
#     words = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
#              'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать']
#     if 0 < num < 21:
#         res = words[num]
#     else:
#         if num < 40:
#             res = words[int(str(num)[0])] + 'дцать'
#         elif str(num)[0] == '4':
#             res = 'сорок'
#         elif str(num)[0] == '9':
#             res = 'девяноста'
#         else:
#             res = words[int(str(num)[0])] + 'десят'
#         if str(num)[1] != 0:
#             res = res + ' ' + words[int(str(num)[1])]
#     return res
# n = int(input())
# print(number_to_words(n))
# alphabet = 'qwertyuiopasdfghjklzxcvbnm'
# print(alphabet)

# def is_pangram(text):
#     alphabet = []
#     new_text = text.strip()
#     for i in range(len(new_text)):
#         if new_text[i] == ' ':
#             continue
#         if new_text[i].lower() not in alphabet:
#             alphabet.append(new_text[i].lower())
#     return len(alphabet) == 26
        
# text = 'Jackdaws love my big sphinx of quartz'
# print(is_pangram(text))

# words = ['Твое число меньше загаданного. попробуй ещё, В следующий раз обязательно повезет', 
#         'Поздравляю! Ты угадал число'
#         'Твое число больше загаданного. попробуй ещё, в следующий раз обязательно повезет!']

# from random import *

# print('Добро пожаловать в числовую угадайку')

# def is_valid(n, rang_e):
#     if n.isdigit():
#         return n in range(1, rang_e+1)

# def comparison(hid_num_in_str, ent_num):
#     hid_num = int(hid_num_in_str)
#     if hid_num == ent_num:
#         return 1
#     elif hid_num < ent_num:
#         return 0
#     elif hid_num > ent_num:
#         return 2

# def mein_func(true_num, hid_num, hid_range):
#     if is_valid(true_num):
#         print(words[comparison(true_num, hid_num)])
#         if comparison(true_num, hid_num) != 1:
#             next_num = input()
#             mein_func(next_num, hid_num)
#     else:
#         print(f'Может быть все-таки целое число от 1 до {hid_range}')
#         next_num = input()
#         mein_func(next_num, hid_num, hid_range)

# def game():
#     print('Введите конец диапазона для загадывания числа, если значение пустое, то диапазон [1, 100]')
#     hid_range = input()
#     if hid_range == '':
#         hid_range = 100
#         hid_num = randint(1, hid_range + 1)
#     else:
#         hid_num = randint(1, int(hid_range)+1)
#     print(f'Введите целое число в диапазоне от 1 до {hid_range}, попробуйте угадать загаданное число')
#     ent_num = input()
#     mein_func(ent_num, hid_num, hid_range)
#     print('Чтобы начать заново, введите "1"', 'Чтобы закончить, введите "0"', sep='\n')
#     answer = input()
#     if answer == '1':
#         game()
#     elif answer == '0':
#         return None

# game()

# rus_alp = ['a', 'b', 'c']

# test = rus_alp
# print(test)

# def shifrator(text, step, temp):
#     result = ''
#     for i in range(len(text)):
#         if text[i].lower() not in temp:
#             result += text[i]
#         else:
#             if text[i].islower():
#                 result += temp[(len(temp) + temp.index(text[i])+step) % len(temp)]
#             else:
#                 result += temp[(len(temp) + temp.index(text[i].lower())+step) % len(temp)].upper()
#     return result

# def shifr(text):
#     if text[0].lower() in rus_alp:
#         temp = rus_alp
#     else:
#         temp = eng_alp
#     text = text.split()
#     for i in range(len(text)):
#         result = [shifrator(text[i], len(text[i]), temp) for i in range(len(text))]
#     return result

# print(*shifr(input()))
alp = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
print(alp)
x = 1000
temp_result = []
while x != 0:
    temp_result.append(alp[x%16])
    x = x // 16
result = ''.join([temp_result[len(temp_result)-i-1] for i in range(len(temp_result))])
print(result)