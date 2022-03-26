import socket, threading
from socketserver import HOST, PORT, enc, dec

client_socket = socket.socket()
client_socket.timeout()

client_socket.connect((HOST, PORT))

def user_auth(client_socket):
    while True:
        recv_msg = dec(client_socket.recv(1024))
        if recv_msg == "0 Auth ok":
            print(recv_msg)
            return True
        elif recv_msg[0] == "1":
            print(recv_msg)
            return False
        else:
            name = input(recv_msg)
            client_socket.send(enc(name))

def user_choice():
    while True:
        users_string = dec(client_socket.recv(1024))
        users_list = [users_string.split('\n')]
        for line in users_list:
            print(users_list.index(line), line)
        selected_user = input\
            ('Select the user you want to chat with: ')
        client_socket.send(enc(selected_user))
        
        

try:
    auth = user_auth(client_socket)
    if auth:
        while True:
            msg = input('\nType ur msg: \n')
            client_socket.send(enc(msg))
            if msg == 'q':
                break
        
    # while True:
    #     message = client_socket.recv(1024)
    #     if message.decode('utf-8') == 'quit':
    #         break
    #     print(message.decode('utf-8'))
        
except KeyboardInterrupt:
    print('n\Client shut down!')
    client_socket.send(enc('q'))
    client_socket.close()
except Exception as e:
    print(e)
    client_socket.close()
client_socket.close()