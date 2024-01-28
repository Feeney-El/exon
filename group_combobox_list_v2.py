import urllib.request, json


def get_providers_info(port=9090) -> dict:
    req = urllib.request.Request(url='http://localhost:%d/proxies' % port
                                 , method='GET')

    f = urllib.request.urlopen(req)

    proxies = f.read().decode('utf8')
    print(f.status)
    print(proxies)
    print(type(proxies))
    proxies_json = json.loads(proxies)
    print(type(proxies_json))
    print(proxies_json['proxies']['GLOBAL']["all"])
    print(type(proxies_json['proxies']['GLOBAL']["all"]))
    print(proxies_json['proxies'].keys())

    group_and_type_dict = {}

    group_list_in_combobox = []
    for i in proxies_json['proxies']['GLOBAL']["all"]:
        # print(i)
        if proxies_json["proxies"][i]["type"] == "Selector" :
            print(i)
            group_and_type_dict[i] = "Selector"
        elif proxies_json["proxies"][i]["type"] == "URLTest":
            print(i)
            group_and_type_dict[i] = "URLTest"

    group_list_in_combobox = list(group_and_type_dict.keys())

    return group_and_type_dict





if __name__ == '__main__':
    get_providers_info()
