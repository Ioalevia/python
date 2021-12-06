class Matrix:
    def __init__(self, arg):
        self.matrix = arg

    def __str__(self):
        a = ''
        for i in self.matrix:
            if self.matrix.index(i) + 1 != len(self.matrix):
                a += '\t'.join(map(str, i))
                a += '\n'
            else:
                a += '\t'.join(map(str, i))
        return a
    def __add__(self, other):
        b = ''
        if len(self.matrix) == len(other.matrix):
            for x, y in zip(self.matrix, other.matrix):
                if len(x) == len(y):
                    list = [num1 + num2 for num1, num2 in zip(x, y)]
                    if self.matrix.index(x) + 1 != len(self.matrix):
                        b += '\t'.join(map(str, list))
                        b += '\n'
                    else:
                        b += '\t'.join(map(str, list))
                else:
                    raise AttributeError(f'Матрицы имеют разный размер')
        else:
            raise AttributeError(f'Матрицы имеют разный размер')
        return b



matrix = Matrix([[1, 2, 3, 5], [4, 5, 6, 7], [7, 8, 9, 10],[10, 11, 12, 13]])
matrix2 = Matrix([[11, 12, 13, 14], [14, 15, 16, 17], [17, 18, 19, 20], [20, 21, 22, 23]])
print(f'{matrix}\n\n{matrix2}\n\n{matrix + matrix2}')