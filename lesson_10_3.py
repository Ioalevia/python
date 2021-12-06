class Cell:
    def __init__(self, num_cells):
        self.cells = int(num_cells)
    def __add__(self, other):
        return Cell(self.cells + other.cells)
    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            raise ArithmeticError(f'операция невозможна')
    def __mul__(self, other):
        return Cell(self.cells * other.cells)
    def __truediv__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells // other.cells)
        else:
            raise ArithmeticError(f'пустая клетка')
    def __floordiv__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells // other.cells)
        else:
            raise ArithmeticError(f'пустая клетка')
    def make_order(self, arg):
        a = str(('*' * arg + '\n') * (self.cells // arg) + ('*' * (self.cells % arg)))
        print(a)


cell = Cell(40)
cell2 = Cell(30)
print(cell.cells)
print(cell2.cells)
print((cell + cell2).cells)
print((cell - cell2).cells)
print((cell * cell2).cells)
print((cell / cell2).cells)
print((cell // cell2).cells)
cell.make_order(9)