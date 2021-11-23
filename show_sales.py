import sys
request = sys.argv[1:]
with open('bakery.csv', 'r', encoding='utf-8') as bakery:
    l = 1
    if len(request) == 0:
        for line in bakery:
            print(line.strip())
    elif len(request) == 1:
        for line in bakery:
            if l >= int(request[0]):
                print(line.strip())
                l = l + 1
            else:
                l = l + 1
    elif len(request) == 2:
        for line in bakery:
            if int(request[1]) >= l >= int(request[0]):
                print(line.strip())
                l = l + 1
            else:
                l = l + 1