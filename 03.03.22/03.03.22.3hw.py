import os
import subprocess

def hw():
    commands = subprocess.getoutput('cat ~/.bash_history').split('\n')
    leng = len(commands)
    print('y == выполнить, n == далее, q = выйти')
    for i in range(leng, 0, -1):
        print(f'command {leng - i}: ', commands[i-1])
        answ = input()[0].lower()
        if answ == 'y':
            os.system(commands[i-1])

hw()