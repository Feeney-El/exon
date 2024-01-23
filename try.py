
import urllib2
import json


def change_proxy(group_name="ChatGPT%E5%8F%8A%E5%85%B6%E4%BB%96AI", server_name="Hong Kong-05"):

    data = {"name" :  server_name}

    # data = urllib.parse.urlencode(data).encode("utf8")
    # data = json.dumps(data)
    # req_before = urllib.request.Request('http://127.0.0.1:9090/proxies/%s' % group_name
    #                              # , data=data
    #                              , method='OPTIONS'
    #                              )

    # g = urllib.request.urlopen(req_before)
    # print(f.status)


    req = urllib2.Request('http://127.0.0.1:9090/proxies/%s' % group_name
                                 , data=data
                                 , method='PUT'
                                 , headers={'Content-Type': 'application/json'}
                                 )
    print(req)
    f = urllib2.urlopen(req)
    print(f.status)
    proxies = f.read().decode('utf8')
    print(proxies)

if __name__ == "__main__":
    change_proxy()