duration = int(input('введите длительность: '))
if duration > 86400:
    d = duration // 86400
    h = duration % 86400 // 3600
    m = duration % 86400 % 3600 // 60
    s = duration % 60
else:
    d = 0
    h = duration // 3600
    m = duration % 3600 // 60
    s = duration % 60
if d > 0:
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
elif h > 0:
    print(h, 'час', m, 'мин', s, 'сек')
elif m > 0:
    print(m, "мин", s, 'сек')
else:
    print(s, 'сек')
