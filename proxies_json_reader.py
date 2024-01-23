import json, get_proxies_info


def get_providers_name() -> list:
    proxies_providers = json.loads(get_proxies_info.get_providers_info())

    # print(proxies_providers["providers"].keys())
    # print(type(proxies_providers))
    # print(type(proxies_providers['providers'].keys()))
    # servers_in_one_provider_group = proxies_providers["providers"][provider_group_name]['proxies'][0]['all']
    # print(servers_in_one_provider_group)
    # print(proxies_providers['providers'][list(proxies_providers["providers"].keys())[0]]['proxies'][0]['all'])
    return list(proxies_providers["providers"].keys())


def get_server_list_in_provider_group(provider_group_name='国外流量') -> list:
    proxies_providers = json.loads(get_proxies_info.get_providers_info())
    all_proxies_data_in_the_group = proxies_providers["providers"][provider_group_name]['proxies']
    print(type(all_proxies_data_in_the_group))
    servers_names_in_this_group = []
    for i in all_proxies_data_in_the_group:
        servers_names_in_this_group.append(i['name'])
    print(servers_names_in_this_group)
    return servers_names_in_this_group


if __name__ == "__main__":
    # get_providers_name()
    # print(type(get_providers_name()))
    print(get_providers_name())
    get_server_list_in_provider_group()