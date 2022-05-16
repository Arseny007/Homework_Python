import sqlite3
# path = '/home/arseny/Homework_python/victorina/database'
path = 'testdb'
def code():
    connection = sqlite3.Connection(database = 'testdb')
    cursor = connection.cursor()
    cursor.execute('drop table questions')
    cursor.execute('create table questions(question text, tour int, qid int autoincrement)')
    cursor.execute('insert into questions (question, tour) values ("97654321 * 9 = ", 1),\
        ("Ты спишь в комнате с холодильником и шкафом, проснувшись, что откроешь первым?", 1),\
        ("Наполнение 3", 2),\
        ("Наполнение 4", 2),\
        ("Наполнение 5", 3),\
        ("Наполнение 6", 3),\
        ("Наполнение 7", 4),\
        ("Наполнение 8", 4),\
        ("Наполнение 9", 5),\
        ("Наполнение 10", 5)')

if __name__ == '__main__':
    code()