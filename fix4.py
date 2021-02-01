import json


def parse_obj(dct):
    for key in dct:
        if isinstance(dct[key], str):
            dct[key] = dct[key].encode('latin_1').decode('utf-8')
        pass
    return dct


with open('./message_1.json', 'r') as f:
    string = json.dumps(json.load(f, object_hook=parse_obj), indent=4)
    with open('./message_1_fixed.json', 'w') as out:
        print(string, file=out)
