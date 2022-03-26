import tarfile, argparse, sys, os


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args(sys.argv[1:])

def solution():
    tname = args.file.split('.')[0] + '.tar.gz' 
    t = tarfile.open(tname, 'w|gz')
    t.add(args.file)
    t.close()
    return

solution()