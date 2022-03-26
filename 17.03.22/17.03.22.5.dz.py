import os, tarfile

def archivator(path):
    t = tarfile.open(path + 'arcvhive.tar.gz', 'w|gz')
    obj = os.walk(path)
    for ff in obj:
        for folder in ff[1]:
            t.add(folder)
        for file in ff[2]:
            t.add(file)
    t.close()

archivator('/home/arseny/papka1')