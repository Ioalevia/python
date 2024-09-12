number = []
# list = []
number_sum_1 = 0
number_sum_2 = 0
for b in range(1, 1000, 2):
    number.append(b**3)
for i in number:
    number_2 = i
    summa = 0
    while i > 0:
        digit = i % 10
        summa = summa + digit
        i = i // 10
    if summa % 7 == 0:
        number_sum_1 = number_sum_1 + number_2
        # print(number_2)
        # list.append(number_2)
# print(sum(list))
print(number_sum_1)
# list.clear()
for i in number:
    i = i + 17
    number_2 = i
    suma = 0
    while i > 0:
        digit = i % 10
        suma = suma + digit
        i = i // 10
    if suma % 7 == 0:
        number_sum_2 = number_sum_2 + number_2
        # print(number_2)
        # list.append(number_2)
# print(sum(list))
print(number_sum_2)