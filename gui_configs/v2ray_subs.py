import base64, json
from urllib.parse import urlsplit

with open("./config_v2ray/FlyingBird_1708321589.txt") as f:
    v2ray_content = f.read()

share_links = base64.b64decode(v2ray_content).decode("utf-8").splitlines()

configs = []
# print(share_links)
for i in share_links:
    url = urlsplit(i)
    url_netloc = url.netloc
    print(url, 'pppppppppppppppp')
    print((url_netloc))
    if len(url.netloc) % 4 > 0:
        padding_count = 4 - (len(url_netloc) % 4)
        url_netloc += "=" * padding_count
    print(base64.b64decode(url_netloc).decode('utf8'))
    configs.append(json.loads(base64.b64decode(url_netloc).decode("utf-8")))
print(configs)
