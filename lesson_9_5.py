class Stationery:
    title = 'Отрисовка'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

a = Stationery()
print(a.title)
a.draw()

b = Pen()
print(b.title)
b.draw()

c = Pencil()
print(c.title)
c.draw()

d = Handle()
print(d.title)
d.draw()