import urllib.request, json, logging, requests
import time

def get_providers_info(port=9090) -> dict:


    logging.basicConfig(filename='./pvc.log'
                        , filemode='a'
                        , format='%(asctime)s  %(filename)s  %(funcName)s  %(levelname)s  %(message)s'
                        , datefmt='%Y-%m-%d %H:%M:%S')


    time.sleep(0.2)
    req = urllib.request.Request(url='http://127.0.0.1:%d/proxies' % port
                                 , method='GET')

    f = urllib.request.urlopen(req)

    

    proxies = f.read().decode('utf8')
    print(f.status)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if f.status == 200:
        logger.info(msg='GET http://localhost:%d/proxies' % port + " the status code is %d" % f.status)
    else:

        logger.error(msg='GET http://localhost:%d/proxies' % port + " the status code is %d" % f.status)

    print(proxies)
    print(type(proxies))

    # logging.info("the GLOBAL proxies are", proxies, "the type is ", type(proxies))
    proxies_json = json.loads(proxies)
    # print(type(proxies_json))
    # print(proxies_json['proxies']['GLOBAL']["all"])
    # print(type(proxies_json['proxies']['GLOBAL']["all"]))
    # print(proxies_json['proxies'].keys())

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
