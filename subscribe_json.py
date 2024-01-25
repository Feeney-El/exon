import json

def write_json(group_name='345', group_link=''):
    dictionary = {
        group_name : group_link
    }

    subscribe_dict = json.load(open("subscribe_json.json"))

    print(subscribe_dict)

    for keys in list(subscribe_dict.keys()):
        if keys == group_name:
            return 0
    # Serializing jsonc
    subscribe_dict[group_name] = group_link



    json_object = json.dumps(subscribe_dict, indent=4)

    with open("subscribe_json.json", "w") as outfile:
        outfile.write(json_object)

    return 1



if __name__ == '__main__':
    write_json(group_name='fl2y123in2g', group_link='')
    print(write_json(group_name='fl2y11111ing', group_link=''))











