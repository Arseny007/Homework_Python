import sys, os, tarfile, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--directory', '-dir')
parser.add_argument('--archive', '-ar', default='archive.tar.gz')
args = parser.parse_args(sys.argv[1:])

def archivator(args):
    tar = tarfile.open(args.archive, 'w|gz')
    for root, d, files in os.walk(args.directory):
        for file in files:
            tar.add(os.path.join(root, file))
    tar.close()

archivator(args)