library = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'}
number = input('enter the number: ')
def num_transle_adv(number):
    for sign in number.split():
        if sign[0].isupper():
            print(str(library.get(number.lower(), None)).title())
        else:
            print(library.get(number, None))
num_transle_adv(number)