for i in range(1, 101, 1):
    a = i % 100
    if a > 10 and a < 20:
        b = 'процентов'
        print(i, b)
    elif i % 10 == 0 or i % 10 == 5 or i % 10 == 6 or i % 10 == 7 or i % 10 == 8 or i % 10 == 9:
        b = 'процентов'
        print(i, b)
    elif i % 10 == 1:
        b = 'процент'
        print(i, b)
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        b = 'процента'
        print(i, b)