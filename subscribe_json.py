import json

def write_json(group_name='', group_link=''):
    dictionary = {
        "group_name": group_name,
        "link": group_link
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("subscribe_json.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == '__main__':
    write_json(group_name='flying'
               , group_link='')











