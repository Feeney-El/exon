import requests, json, urllib.parse
import urllib.request


class ApiRequest():

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


    def get_providers_info(port=9090):
        req = urllib.request.Request(url='http://localhost:%d/providers/proxies' % port
                                     , method='GET')

        f = urllib.request.urlopen(req)

        proxies = f.read().decode('utf8')
        print(f.status)
        print(proxies)
        print(type(proxies))
        return proxies


    def change_proxy(group_name="ChatGPT及其他AI", server_name="Hong Kong-05"):
        group_name_url_code = urllib.parse.quote_plus(group_name)

        data = {"name": server_name}
        print(group_name_url_code)
        resp = requests.put(
            url='http://127.0.0.1:9090/proxies/%s' % group_name_url_code,
            data=json.dumps(data)
        )

        print(resp.status_code)

    def change_allow_lan(change_to=False):
        url_lan = "http://127.0.0.1:9090/configs"
        data = {"allow-lan": change_to}
        resp = requests.patch(
            url=url_lan,
            data=json.dumps(data)
            # data=data
        )

        print(resp.text)
        print(resp.status_code)

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



    def change_proxy_mode(change_to="Global"):
        url_lan = "http://127.0.0.1:9090/configs"
        data = {"mode": change_to}
        resp = requests.patch(
            url=url_lan,
            data=json.dumps(data)
            # data=data
        )
        print(change_to)
        print(resp.text)
        print(resp.status_code)




