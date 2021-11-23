import sys
file, request = sys.argv
with open('bakery.csv', 'a', encoding='utf-8') as bakery:
    bakery.write(str(request) + '\n')