import re

def email_parse(a):
    email = {}
    RE_ADR = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-+.]+\.[a-zA-Z0-9-]+$')
    try:
        adr = RE_ADR.findall(a)
        if len(adr) == 0:
            raise ValueError(f'wrong email: {a}')
        for i in adr:
            email.setdefault('username', i.split('@')[0])
            email.setdefault('domain', i.split('@')[1])
            print(email)
    finally:
        print('')
email_parse(input('введите email: '))