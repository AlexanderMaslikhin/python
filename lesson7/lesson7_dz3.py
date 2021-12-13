class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count > other.cell_count:
            return Cell(self.cell_count - other.cell_count)
        else:
            print('Вычитание невозможно')

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def make_order(self, row_len):
        if self.cell_count // row_len:
            result = '\n'.join(['*' * row_len for _ in range(self.cell_count // row_len)])
            if self.cell_count % row_len:
                result += '\n' + '*' * (self.cell_count % row_len)
        else:
            result = '*' * self.cell_count
        return result



c1 = Cell(10)
c2 = Cell(25)
print((c1 + c2).make_order(7), end='\n-----\n')
print((c1 * c2).make_order(30), end='\n-----\n')
print((c2 / c1).make_order(2), end='\n-----\n')
print((c2 - c1).make_order(4), end='\n-----\n')
