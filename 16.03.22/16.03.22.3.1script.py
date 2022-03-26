import sys
import argparse
import os

class FileNotFound(Exception):
    pass

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', default='/home/arseny/')
parser.add_argument('-s', '--source')
args = parser.parse_args(sys.argv[1:])

def find_path(name):
    args = sys.argv[1:]
    if name in args:
        file_index = args.index(name)+1
        if file_index < len(args):
            file = args[file_index]
            if os.path.exists(name) and os.path.isfile(name):
                return file
    raise FileNotFound

def script():
    source = find_path('--source')
    output = find_path('--output')
    f = open(source, 'r')
    for line in f:
        result += line + '\n'
    with open(output, 'w') as f1:
        f1.write(result)

    f.close()
    return
