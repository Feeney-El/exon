import urllib.request


def get_providers_info(port=9090):
    req = urllib.request.Request(url='http://localhost:%d/providers/proxies' % port
                                 , method='GET')

    f = urllib.request.urlopen(req)

    proxies = f.read().decode('utf8')
    print(f.status)
    print(proxies)
    print(type(proxies))
    return proxies



if __name__ == "__main__":
    get_providers_info()

