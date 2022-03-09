import os

def func(file):
    result, names = [], []
    obj = os.stat(file)
    result.append(obj.st_uid)
    result.append(obj.st_gid)
    result.append(obj.st_mtime)
    result.append(obj.st_size)

    return result, names

# func('/home/arseny/fileee.txt')

def print_sorted(direc):
    files = os.listdir(direc)
    dict_files = {}
    for fn in files:
        dict_files[fn] = (os.stat(direc + '/' + fn)).st_mtime
    # dict_filess = {fn:(os.stat(fn)).st_mtime for fn in files}
    items = dict_files.items()
    items = sorted(items, key = lambda x: x[1])
    for pair in items:
        print(pair[0])

print_sorted("/home/arseny/papka1")