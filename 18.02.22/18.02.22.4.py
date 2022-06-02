import os

def reinfo(name, old_data, new_data):
    if os.path.exists(name) and name[-4:] == '.txt' and os.path.isfile(name):
        with open ('/home/arseny/filefile.txt', 'r') as f:
            old_data = f.read()
        result = old_data.replace(old_data, new_data)
        with open ('/home/arseny/filefile.txt', 'w') as f:
            f.write(result)
    else:
        print('неправильно')

reinfo('/home/arseny/filefile.txt', 'dog', 'cat')