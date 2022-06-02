import string

alph_low = string.ascii_lowercase
alph_up = string.ascii_lowercase
length = len(alph_low)

class Rot:
    @staticmethod
    def encode(data, num):
        result = ''
        for i in data:
            if i in alph_low:
                temp = alph_low.index(i) + num
                if temp < 0:
                    temp += length
                elif temp > length - 1:
                    temp -= length
                result += alph_low[temp]
            elif i in alph_up:
                temp = alph_up.index(i) + num
                if temp < 0:
                    temp += length
                elif temp > length - 1:
                    temp -= length
                result += alph_up[temp]
            else:
                result += i
        return result

    def decode(data, num):
        return Rot.encode(data, num)

print(Rot.decode('abc', 10))