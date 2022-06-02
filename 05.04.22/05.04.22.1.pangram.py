import string

def pangram(data):
    alph = string.ascii_lowercase
    len_alph = len(alph)
    count = 0
    letters = [i for i in data if i.lower() in alph]
    setdata = set(data)
    for i in setdata:
        if i in alph:
            count += 1
    return count == len(alph)

        

print(pangram('The quick brown fox jumps over the lazy dog'))