mem = [0] * 1000
res = 0
def func(n):
    if n < 11:
        mem[n] = n * 2
        return n * 2
    elif n % 3 == 0:
        mem[n] = mem[n//11] * n - n * 3
        return mem[n]
    elif n % 3 == 1:
        mem[n] = mem[n//11] // n + n * n
        return mem[n]
    elif n % 3 == 2:
        mem[n] = 30
        return 30

for i in range(1000):
    func(i)
for i in range(len(mem)):
    c = 0
    for j in range(len(str(mem[i]))):
        if str(mem[i])[j] == '3':
            c += 1
    if c >= 3:
        res += 1
print(res)
