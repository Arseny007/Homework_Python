import tarfile
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args(sys.argv[1:])

t = tarfile.open('new.tar.gz', 'w|gz')
t.add('new.txt')
t.close()