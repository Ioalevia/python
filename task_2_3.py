list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
a = str()
for i in list:
    try:
        if '+' in i:
            i = int(i)
            if i < 10:
                i = str(i)
                i = '0' + i
                i = '+' + i
                a = a + ('"' + i +'" ')
            else:
                a = a + ('"' + i + '" ')
        else:
            i = int(i)
            if i < 10:
                i = str(i)
                i = '0' + i
                a = a + ('"' + i + '" ')
            else:
                a = a + ('"' + i + '" ')
    except:
        i = str(i)
        a = a + i + ' '
print(a)