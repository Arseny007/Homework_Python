import tarfile

# t = tarfile.open('archive.tar', 'w|gz')

f = open('new.txt', 'w')
s = 'Это текстовая трока'
for i in range(1000):
    f.write(s + '\n')
    print(i)
f.close()