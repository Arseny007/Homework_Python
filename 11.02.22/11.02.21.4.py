# задание 1: ф. для инстаграма
# принимать список пользователей

def solution_first(names):
    count_names = len(names)
    if count_names < 1:
        return None 
    elif count_names == 1:
        return f'{names[0]} likes it'
    elif count_names == 2:
        return f'{names[0]} and {names[1]} likes it'
    elif count_names == 3:
        return f'{names[0]}, {names[1]} and {names[2]} likes it'
    else:
        result = f'{names[0]} and ' + str(count_names - 1) + ' people likes it'
        return result

def solution_second(names):
    count_names = len(names)
    if count_names < 1:
        return None 
    elif count_names == 1:
        return '{0[0]:} likes it'.format(names)
    elif count_names == 2:
        return '{0[0]:} and {0[1]:} likes it'.format(names)
    elif count_names == 3:
        return '{0[0]:}, {0[1]:} and {0[2]:} likes it'.format(names)
    else:
        return '{0:} and {1:} people likes it'.format(names[0], count_names - 1)

def solution_third(names):
    count_names = len(names)
    if count_names < 1:
        return None 
    elif count_names == 1:
        return '%s likes it'%(names[0])
    elif count_names == 2:
        return '%s and %s likes it'%(names[0], names[1])
    elif count_names == 3:
        return '%s, %s and %s likes it'%(names[0], names[1], names[2])
    else:
        return '%s and %d people likes it'%(names[0], count_names - 1)

names0 = []
names = names0 + ['Putin']
names1 = names + ['Jesus']
names2 = names1 + ['Arseny']
names3 = names2 + ['Elon']
print(solution_first(names0))
print(solution_first(names))
print(solution_first(names1))
print(solution_first(names2))
print(solution_first(names3))
print(solution_second(names0))
print(solution_second(names))
print(solution_second(names1))
print(solution_second(names2))
print(solution_second(names3))
print(solution_third(names0))
print(solution_third(names))
print(solution_third(names1))
print(solution_third(names2))
print(solution_third(names3))