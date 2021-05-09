import json
import datetime as datetime
import time


# read facebook files and convert to json
def read_json(filename: str) -> json:
    with open(filename) as file:
        data = json.load(file)
        return data


# change given "normal" date to unix value
def date_to_unix(date_values: list[int]):
    return int(time.mktime(datetime.datetime(date_values[0], date_values[1], date_values[2], 0, 0).timetuple()) * 1000)


# convert dictionaries to list for better data reading for graphs
def convert_to_list(data: json) -> list:
    my_return = list(data.items())
    my_return.sort(key=lambda my_tuple: my_tuple[1])
    return my_return


# export results to .csv file
def export_to_csv(messages, filename: str):
    with open(filename, 'w', encoding="utf-8") as my_file:
        my_file.write("Username" + ";" + "messages" + "\n")
        for output in messages:
            my_file.write(output[0] + ";" + str(output[1]) + "\n")


# display dictionary
def printing_dict(messages: dict):
    for user in messages:
        print(user)
