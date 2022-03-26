import socket, sqlite3
from pprint import pprint
import threading
users = dict()
HOST = '127.0.0.1'
PORT = 12345

def enc(s):
    return s.encode('utf-8')

def dec(s):
    return s.decode('utf-8')

def server_auth(user):
    while True:
        cursor.execute('select * from banlistport')
        for banaddressport in cursor.fetchall():
            if banaddressport == address:
                user.send(enc('1 You are banned by ip. You will be disabled'))
                print(f"user with ip:port: {address} - tried to connect")
                return 0, 'Nothing'
        else:
            user.send(enc("Type your name: "))
            username = dec(user.recv(1024))
            cursor.execute('select * from banlistnickname')
            banlistnames = cursor.fetchall()
            for bannickname in banlistnames:
                if bannickname[0] == username:
                    user.send(enc("1 This name is banned. You will be disable"))
                    print(f"user {username} tried to connect")
                    return 0, username
            else:
                if username not in users.keys():
                    print('User {0[0]}:{0[1]} connected as {1}'\
                        .format(address, username))

                print('\nNow connected: \n')
                print(users)
                user.send(enc('0 Auth ok'))
                return True, username

def user_choices():
    users_list = '\n'.join(user.keys())
    user.send(enc(users_list))
    selected_user = dec(user.recv(1024))
    

def new_client(client_socket, username):
    global users
    while True:
        recv_msg = client_socket.recv(1024)
        decoded = dec(recv_msg)
        print('User {0}:{1}'. format(username, decoded))
        print('\n', users)

        if decoded == 'q':
            del users[username]
            print('User {0} disconnected'.format(username))
            print(users)
            break

if __name__ == '__main__':
    connection = sqlite3.connect(database = '/home/arseny/banlist_bd')
    cursor = connection.cursor()
    cursor.execute('drop table if exists "banlistport";')
    cursor.execute('create table "banlistport" ("address" text,"port" text);')
    for i in range(20):
        cursor.execute(f'insert into "banlistport" values ("127.0.0.1",{650+i});')
    cursor.execute('drop table if exists "banlistnickname";')
    cursor.execute('create table "banlistnickname" (name text);')
    cursor.execute('insert into "banlistnickname" values ("arseny");')

    server_socket = socket.socket()

    server_socket.bind((HOST, PORT))
    server_socket.listen()

    try:
        while True:
            user, address = server_socket.accept()
            print('\nConnected: ', address)
            success_connect, username = server_auth(user)
            if success_connect:
                users[username] = address
                threading.Thread(target = new_client, \
                    args = (user, username)).start()

    except KeyboardInterrupt:
        print('n\Server shut down!')
        server_socket.close()

    except Exception as e:
        print(e)
        server_socket.close()
    server_socket.close()

    connection.commit()

    cursor.close()
    connection.close()  