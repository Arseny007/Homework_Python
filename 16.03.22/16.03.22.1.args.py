import sys
import os

class SourceNotFound(Exception):
    pass

class SourceCantBeLast(Exception):
    pass

def check_source():
    args = sys.argv[1:]
    if '--source' in args:
        source_index = args.index('--source')+1
        if source_index < len(args):
            return args[source_index]
        elif source_index == len(args):
            raise SourceCantBeLast
    raise SourceNotFound

print(check_source())