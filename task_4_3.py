from requests import get, utils
from datetime import date
def currency_rates(x):
    xml_list = []
    currency_dict = {}
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    xml_list = content.replace("<", " ").replace(">", " ").replace(",", ".").split()
    date_full = xml_list[4].split('"')
    date_split = date_full[1].split('.')
    date_format = date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
    i = 0
    x = str(x).upper()
    while i < len(xml_list):
        if xml_list[i] == 'CharCode':
            currency_dict.setdefault(xml_list[i + 1], xml_list[i + 11])
            i = i + 1
        else:
            i = i + 1
    if x in currency_dict:
        print(f'{float(currency_dict[x])}, {date_format}')
    else:
        print('None')

currency_rates('ByN')
currency_rates('USD')
currency_rates('uah')