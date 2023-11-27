import json
import sys


def parse_obj(dct):
    for key in dct:
        if isinstance(dct[key], str):
            dct[key] = dct[key].encode("latin_1").decode("utf-8")
        pass
    return dct


def main():
    if len(sys.argv) < 3 or sys.argv[1][0] == "-":
        print("Usage:" + sys.argv[0] + "  <input> <output>")
    else:
        filename_in = sys.argv[1]
        filename_out = sys.argv[2]
        with open(filename_in, "r") as f:
            string = json.dumps(json.load(f, object_hook=parse_obj), indent=4)
            with open(filename_out, "w") as out:
                print(string, file=out)


if __name__ == "__main__":
    main()
