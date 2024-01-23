import urllib.request, json


def get_config() -> dict:

    url_config = 'http://127.0.0.1:9090/configs'
    req = urllib.request.Request(url=url_config
                                 , method='GET')

    f = urllib.request.urlopen(req)

    configs = f.read().decode('utf8')
    configs = json.loads(configs)
    print(f.status)
    print(configs)
    print(type(configs))
    return configs


if __name__ == "__main__":
    get_config()
