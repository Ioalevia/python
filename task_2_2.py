list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []
for i in list:
    try:
        if '+' in i:
            i = int(i)
            if i < 10:
                i = str(i)
                i = '0' + i
                i = '+' + i
                list_2.append('"')
                list_2.append(str(i))
                list_2.append('"')
            else:
                list_2.append('"')
                list_2.append(str(i))
                list_2.append('"')
        else:
            i = int(i)
            if i < 10:
                i = str(i)
                i = '0' + i
                list_2.append('"')
                list_2.append(str(i))
                list_2.append('"')
            else:
                list_2.append('"')
                list_2.append(str(i))
                list_2.append('"')
    except:
        list_2.append(i)
print(list_2)
final = ' '.join(list_2)
print(final)