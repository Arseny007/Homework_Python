import os
def check():
    obj = os.uname()
    print(obj.sysname, obj.version, sep = '\n')
    if obj.sysname == 'Linux':
        return True
    

print(check())