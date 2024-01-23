import urllib.request, json, urllib.parse



def speed(server_name='Hong Kong-09') -> tuple:


    server_name_url_encode = urllib.parse.quote(server_name)
    print(server_name_url_encode)
    url = "http://127.0.0.1:9090/proxies/%s/delay?timeout=5000&url=http://www.gstatic.com/generate_204" % server_name_url_encode

    req = urllib.request.Request(url=url
                                 , method='GET')
    f = urllib.request.urlopen(req)

    speed_dict = f.read().decode('utf8')
    print(f.status)
    print(json.loads(speed_dict))
    print(type(json.loads(speed_dict)))
    return json.loads(speed_dict)['delay'], json.loads(speed_dict)['meanDelay']

if __name__ == "__main__":
    # speed()
    delay, meanDelay = speed()
    print(delay, meanDelay)