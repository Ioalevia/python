import sys
import in_place
request = sys.argv[1:]
with in_place.InPlace('bakery.csv', encoding='utf-8') as bakery:
    l = 1
    for line in bakery:
        line = line.strip()
        if l != int(request[0]):
            bakery.write(line + '\n')
            l = l + 1
        elif l == int(request[0]):
            line = line.replace(line, request[1] + '\n')
            bakery.write(line)
            l = l + 1
    if l < int(request[0]):
        print('wrong number')