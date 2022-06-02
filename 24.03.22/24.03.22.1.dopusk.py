import socket

command = ''
with open ('servers.txt') as file:
    for address in file:
        HOST, PORT = address.split(':')[0], int(address.split(':')[1])
        connection = socket.socket()
        try:
            connection.connect((HOST,PORT))
            connection.settimeout(5)
        except Exception as e:
            print(e)
            print(f'Server {HOST} is unreachable')
        else:
            print(f'Ok {HOST}')
        finally:
            connection.close()