def female(num):
    if num != 0:
        return num - male(female(num-1))
    else:
        return 1


def male(num):
    if num != 0:
        return num - female(male(num-1))
    else:
        return 0

num = int(input('enter num: '))
func = input('input gender m/f: ')
if func == 'm':
    print(male(num))
if func == 'f':
    print(female(num))