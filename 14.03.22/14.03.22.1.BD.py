import sqlite3

def select(table, condition):
    return 'select * from {0} where {1}'.format(table, condition)

def delete(table, condition):
    return 'delete from {0} where {1}'.format(table, condition)

def update(table, atr, value, condition):
    return 'update {0} set {1} = {2} where {3}'.format(table, atr, value, condition)

def insert(table, data):
    return 'insert into {0} values ({1})'.format(table, ' '.join(data))

table = ''
level = 1
menus = [['1. Выбор БД', '2. Выход'], 
        ['1. select', ' 2. update',  '3. delete', '4. insert']]

while True:
    ans = int(input(*menus[level - 1], sep = '\n'))
    if level == 1:
        if ans == '1':
            table = input('Введите название базы данных: ')
            level = 2
        elif ans == '2':
            conctn.commit()
            curs.close()
            conctn.close()
    elif level == 2:
        def execute(query):
            curs.execute(query)
            return curs.fetchall()
        def printOutput(a):
            s = ''
            for i in a:
                for j in i:
                    s += '{0:^25}'.format(j)
                    s += '\n'
            print(s)
        printOutput(execute)
    conctn = sqlite3.connection(database = '14.03.22.1.BD')
    curs = conctn.cursor()
    