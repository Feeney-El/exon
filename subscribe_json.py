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



def read_subscribe_json(file_name="subscribe_json.json") -> list:

    subscribe_dict = json.load(open(file_name))
    tuple_items = subscribe_dict.items()
    print(list(tuple_items))

    list_string = []
    for i in tuple_items:
        tuple_to_string = "".join(str(i))
        list_string.append(tuple_to_string)


    print(list_string)
    return list_string

if __name__ == '__main__':
    # write_json(group_name='fl2y123in2g', group_link='')
    # print(write_json(group_name='fl2y11111ing', group_link=''))

    read_subscribe_json()









