import sqlite3

path = '/home/arseny/Homework_python/victorina/database'

def code():
    connection = sqlite3.Connection(database = path)
    cursor = connection.cursor()
    cursor.execute('create table questions(question text, tour int)')
    cursor.execute('insert into questions values\
        (Вопрос 1, tour 1), (),\
            (')


if __name__ == '__main__':
    code()