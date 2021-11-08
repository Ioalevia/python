list = [58.6, 62.58, 12.03, 789.21, 56, 1.5, 79, 25, 65.04, 22, 99.99, 45, 37.56, 64.64, 11.11, 123.45, 98.76, 55.55, 0.35, 0.89]
print('id списка до сортировки: ' + str(id(list)))
total_1 = []
for price in list:
    price = str(price)
    a = price.split('.')
    if len(a) == 2:
        str_price = a[0] + ' руб ' + a[1] + ' коп '
        total_1.append(str_price)
        if len(a[1]) == 1:
            str_price = a[0] + ' руб ' + a[1] + '0 коп '
            total_1.append(str_price)
    else:
        str_price = a[0] +' руб ' + '00 коп'
        total_1.append(str_price)
total_2 = ', '.join(total_1)
print(total_2)
list.sort()
total_1.clear()
for price in list:
    price = str(price)
    a = price.split('.')
    if len(a) == 2:
        str_price = a[0] + ' руб ' + a[1] + ' коп '
        total_1.append(str_price)
        if len(a[1]) == 1:
            str_price = a[0] + ' руб ' + a[1] + '0 коп '
            total_1.append(str_price)
    else:
        str_price = a[0] +' руб ' + '00 коп'
        total_1.append(str_price)
total_2 = ', '.join(total_1)
print('id списка после сортировки: ' + str(id(list)))
print(total_2)
import copy
list_2 = copy.deepcopy(list)
list_2.reverse()
total_1.clear()
for price in list_2:
    price = str(price)
    a = price.split('.')
    if len(a) == 2:
        str_price = a[0] + ' руб ' + a[1] + ' коп '
        total_1.append(str_price)
        if len(a[1]) == 1:
            str_price = a[0] + ' руб ' + a[1] + '0 коп '
            total_1.append(str_price)
    else:
        str_price = a[0] +' руб ' + '00 коп'
        total_1.append(str_price)
total_2 = ', '.join(total_1)
print('id нового списка: ' + str(id(list_2)))
print(total_2)
print("5 самых дорогих товаров: " + ', '.join(total_1[5::-1]))
