from urllib.request import urlopen
with urlopen("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs") as f:
    dict_ip = {}
    for line in f:
        line = line.strip().decode("utf-8").split(' ')
        remote_addr = line[0]
        request_type = line[5].replace('"', "")
        requested_resource = line[6]
        print((remote_addr, request_type, requested_resource))
        if remote_addr not in dict_ip:
            dict_ip.setdefault(remote_addr, 1)
        else:
            i = int(dict_ip.get(remote_addr))
            i = i + 1
            dict_ip.update({remote_addr:i})
a = max(dict_ip, key=dict_ip.get)
print(f'IP адрес спамера {a}! Он отправил {dict_ip.get(a)} запросов!')