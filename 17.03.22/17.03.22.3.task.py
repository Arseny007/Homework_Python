import tarfile, argparse, sys, os


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-o', '--output', default = 'archive.tar.gz')
args = parser.parse_args(sys.argv[1:])

def solution():
    t = tarfile.open(args.output, 'w|gz')
    t.add(args.file)
    t.close()
    return

solution()