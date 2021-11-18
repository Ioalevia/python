import itertools
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Констанция', 'Ихтиандр'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
result_gen = (i for i in itertools.zip_longest(tutors, klasses))
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))