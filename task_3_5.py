nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
import random
def get_jokes(n, flag=False):
    i = 0
    """функция будет выполняться запрошенное количество раз"""
    while i < n:
        """берем по одному элементу из каждого списка и объединяем в шутку"""
        a = random.choice(nouns)
        b = random.choice(adverbs)
        c = random.choice(adjectives)
        joke = f'{a} {b} {c}'
        print(joke)
        """счстчик, чтобы функция не выполнялась бесконечно"""
        i = i + 1
        """В случае установки флага удаляем отработанные элементы"""
        if flag == True:
            nouns.remove(a)
            adverbs.remove(b)
            adjectives.remove(c)
get_jokes(5, flag=True)
