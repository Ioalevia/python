class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

class Position(Worker):
    def get_full_name(self):
        print(f'{self.surname} {self.name}')
    def get_total_income(self):
        print(f'{sum(self._income.values())}р')

a = Position()
a.name = 'Иван'
a.surname = 'Авалонов'
a.position = 'Строитель'
a._income["wage"] = 1000
a._income["bonus"] = 100
print(f'{a.position} {a.surname} {a.name} с доходом {a._income["wage"]}р и премией {a._income["bonus"]}р')
a.get_full_name()
a.get_total_income()

b = Position()
b.name = 'Геннадий'
b.surname = 'Никонов'
b.position = 'Визажист'
b._income["wage"] = 10000
b._income["bonus"] = 1
print(f'{b.position} {b.surname} {b.name} с доходом {b._income["wage"]}р и премией {b._income["bonus"]}р')
b.get_full_name()
b.get_total_income()