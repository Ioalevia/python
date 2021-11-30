import re
from urllib.request import urlopen
with urlopen("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs") as f:
    RE_ADR = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(\d{1,2}\/\w+\/\d{4}(:\d{2}){3}\s\+\d{4})|(HEAD|GET)|(?<=\s)/\S+(?=|s)|(?<=\s)\d+(?=|s)')
    for line in f:
        line = line.strip().decode("utf-8")
        # print(line)
        # print(*map(lambda x: x.group(0), RE_ADR.finditer(line)), sep=', ')
        a = tuple(map(lambda x: x.group(0), RE_ADR.finditer(line)))
        print(f'parsed_raw = {a}')
