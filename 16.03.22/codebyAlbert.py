import os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', default='/home/arseny/')
parser.add_argument('-s', '--source')
args = parser.parse_args(sys.argv[1:])

def parse_file(filepath,dirpath):
    file_cond = os.path.exists(filepath) and os.path.isfile(filepath)
    dir_cond = os.path.exists(dirpath) and os.path.isdir(dirpath)
    if file_cond and dir_cond:
        if dirpath[-1] != '/':
            dirpath  += '/'
        filepath = filepath[filepath.rfind('/'):]
        with open(filepath, 'r') as fp:
            i = 1
            for line in fp:
                fn, ext = filepath.split('.')
                with open(f'{fn}_{str(i)}.{ext}', 'w') as fw:
                    fw.write(line)
                print('file', i, 'was written\n')
                i += 1
    else:
        print('Source or Output')

