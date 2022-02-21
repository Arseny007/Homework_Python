class Matrix:
    valid = False
    def __init__(self, data):
        if len(data) != 0:
            y = len(data[0])
            for i in data[1:]:
                if len(i) != y:
                    print('Матрица неровная')
                    break
            else:
                self.data = data
                self.valid = True
        else:
            print('Матрица даёт сбои')

    def transpose(self):
        return [list(r) for r in zip(*self.data)]
        
    # def transpose(self):
        # if self.valid:
        #     # result = [[''] * len_stroki] * len_stolba
        #     result = [[]*len((self.data[0]))]
        #     for i in range(len(self.data[0])):
        #         for j in range(len(self.data)):
        #             result[i].append(self.data[j][i])
        #     return result


matrica = [[1, 2, 3],
[4, 5, 6]]

matr = Matrix(matrica)
print(matr.transpose())