import random
import sys
class Card:
    def __init__(self, name):
        self.nums = []
        self.card_list = []
        self.name = name
        while len(self.nums) < 15:
            num = random.randint(1, 90)
            if num not in self.nums:
                self.nums.append(num)
        for i in range(0, 3):
            a = sorted(self.nums[5 * i : 5 * (i + 1)])
            for b in range(0, 4):
                index = random.randint(0, len(a))
                a.insert(index, 0)
            self.card_list += a
    def __str__(self):
        line = '--------------------------'
        card = self.name + ':' + '\n' + line + '\n'
        for index, num in enumerate(self.card_list):
            if num == 0:
                card += '  '
            elif num == -1:
                card += ' -'
            elif num < 10:
                card += f' {str(num)}'
            else:
                card += str(num)

            if (index + 1) % 9 == 0:
                card += '\n'
            else:
                card += ' '
        return card + line
    def cross(self, num):
        for index, item in enumerate(self.card_list):
            if item == num:
                self.card_list[index] = -1
                return
    def __contains__(self, item):
        return item in self.card_list
    def close(self):
        return set(self.card_list) == {0, -1}

class Game:
    def __init__(self, player_1, player_2):
        self.user = player_1
        self.comp = player_2
        self.kegs = []
        while len(self.kegs) < 90:
            num_2 = random.randint(1, 90)
            if num_2 not in self.kegs:
                self.kegs.append(num_2)
    def start(self):
        keg = self.kegs.pop()
        print(player_1)
        print(player_2)
        print(f'Новый бочонок: {keg} (осталось {len(self.kegs)})')
        answer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if answer == 'y' and not keg in self.user or \
           answer != 'y' and keg in self.user:
            sys.exit('Вы проиграли!')
        if keg in self.user:
            self.user.cross(keg)
            if self.user.close():
                sys.exit('Вы победили!')
        if keg in self.comp:
            self.comp.cross(keg)
            if self.comp.close():
                sys.exit('Вы проиграли!')
        game.start()

player_1 = Card('Игрок')
player_2 = Card('Компьютер')
game = Game(player_1, player_2)
game.start()