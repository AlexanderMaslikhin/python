
class Matrix:
    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        self.data = [[None for _ in range(columns)] for _ in range(rows)]
        if data:
            if len(data) != self.rows:
                raise ValueError("Не совпадают размеры матрицы с переданными параметрами")
            for row in data:
                if isinstance(row, list) and len(row) != self.columns:
                    raise ValueError("Не совпадают размеры матрицы с переданными параметрами")
            self.data = data[:][:]

    @property
    def shape(self):
        return self.rows, self.columns

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __getitem__(self, item):
        if isinstance(item, tuple):
            i, j = item
            return self.data[i][j]
        else:
            return self.data[item]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            i, j = key
            self.data[i][j] = value
        else:
            raise IndexError('Индекс матрицы содержит 2 элемента')

    def __add__(self, other):
        if self.shape == other.shape:
            result = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.data, other.data)]
            return Matrix(*self.shape, result)
        else:
            raise ValueError("Размеры матриц не совпадают")


m = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
print(m.shape)
print(f'Элемент матрицы {m[0, 2]}')
print(f'строка матрицы {m[1]}')
print(m)
n = Matrix(2, 3, [[1, 1, 1], [1, 1, 1]])
print(n)
print('Сумма матриц:')
print(m + n)
c = Matrix(2, 2)
print('Пустая матрица')
print(c)
c[0, 1] = 1
c[1, 0] = 2
print(c)

