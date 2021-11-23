from urllib.request import urlopen
with urlopen("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs") as f:
    for line in f:
        line = line.strip().decode("utf-8").split(' ')
        remote_addr = line[0]
        request_type = line[5].replace('"', "")
        requested_resource = line[6]
        print((remote_addr, request_type, requested_resource))