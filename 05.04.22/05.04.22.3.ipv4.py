# def translate(num):
#     binnum = str(bin(num))
#     binnum = binnum[2:]
#     while len(binnum) < 32:
#         binnum = '0' + binnum
#     # address = ['0b' + binnum[:8]), ('0b' + binnum[8:16]), ('0b' + binnum[16:24]), ('0b' + binnum[24:])]
#     address = [str(int('0b' + binnum[:8])), str(int('0b' + binnum[8:16])),\
#         str(int('0b' + binnum[16:24])), str(int('0b' + binnum[24:]))]
#     print(address)
#     return '.'.join(address)
# translate(127)

def f(s):
    bits = '{0:0>32b}'.format(s)
    lis = [bits[i*8:(i+1)*8] for i in range(0,4)]
    for i in range(4):
        lis[i] = str(int(lis[i], 2))
    return '.'.join(lis)

print(f(127))