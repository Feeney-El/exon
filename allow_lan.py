import requests, json, urllib.parse

def change_allow_lan(change_to=False):

    url_lan = "http://127.0.0.1:9090/configs"
    data = {"allow-lan":change_to}
    resp = requests.patch(
        url=url_lan,
        data=json.dumps(data)
        # data=data
    )

    print(resp.text)
    print(resp.status_code)







if __name__ == "__main__":
    change_allow_lan()
