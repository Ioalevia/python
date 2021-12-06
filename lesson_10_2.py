from abc import ABC, abstractmethod

class Clothes(ABC):
    _tot = 0
    full = 0
    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def total(self):
        pass

    @property
    def full_total(self):
        return Clothes.full

class Coat(Clothes):
    def __init__(self, size):
        self.v = size
        self.c = self.v / 6.5 + 0.5
        Coat._tot += self.c
        Clothes.full += self.c

    @property
    def count(self):
        return self.c

    @property
    def total(self):
        return Coat._tot

class Costume(Clothes):
    def __init__(self, height):
        self.h = height
        self.c = 2 * height + 0.3
        Costume._tot += self.c
        Clothes.full += self.c

    @property
    def count(self):
        return self.c

    @property
    def total(self):
        return Costume._tot


coat = Coat(44)
coat2 = Coat(46)
costume = Costume(1.5)
costume2 = Costume(2)
print(coat.count)
print(coat2.count)
print(coat2.total)
print(costume.count)
print(costume2.count)
print(costume2.total)
print(costume2.full_total)
