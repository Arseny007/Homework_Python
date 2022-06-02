# Exception - зарезервированное слово, это все ошибки
# 
# try 
# 
# except Exception as e:
#      print(e):
#           e.data
# 
class OddNumberError(Exception):
    pass

try:
    for i in range(0,10):
        if i % 2 != 0:
            raise OddNumberError
        print(i)
except Exception:
    print('наша ошибка')
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
