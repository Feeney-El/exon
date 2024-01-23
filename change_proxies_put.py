import requests, json, urllib.parse

def change_proxy(group_name="ChatGPT及其他AI", server_name="Hong Kong-05"):

    group_name_url_code = urllib.parse.quote_plus(group_name)

    data = {"name": server_name}
    print(group_name_url_code)
    resp = requests.put(
        url='http://127.0.0.1:9090/proxies/%s' % group_name_url_code,
        data=json.dumps(data)
    )

    print(resp.status_code)







if __name__ == "__main__":
    change_proxy()

