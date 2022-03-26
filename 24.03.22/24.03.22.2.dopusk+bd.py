import socket, sqlite3

command = ''

connection = sqlite3.connect(database = '/home/arseny/db_servers')
cursor = connection.cursor()

cursor.execute('''select * from addresses_db''')
var = cursor.fetchall()

if not var:
    print('db is empty')
else:
    for address in var:
        HOST, PORT = address[0], address[1]
        connection = socket.socket()
        try:
            connection.settimeout(5)
            connection.connect((HOST,PORT))
        except Exception as e:
            print(e)
            print(f'Server {HOST} is unreachable')
        else:
            print(f'Ok {HOST}')
        finally:
            connection.close()