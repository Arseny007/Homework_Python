names = ['Borovoy Arseny Mikhailovich','Putin Vladimir Vladimirovich']

result=[]

def initials(name):
        l = name.split()
        return l[0] + ' ' + l[1][0:1] + '. ' + l[2][0:1] + '.'

def initials_more(names):
    return [initials(name) for name in names]

def decorator(func):
    def inner(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return inner

b=decorator(initials_more)
print(b(names))