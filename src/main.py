import parameters
import datetime as datetime
import time
import os
import json
from src.graphs import draw_plot
from src import calculate as cal


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


# main function
def main():
    my_files_name = []
    os.chdir("../" + values.messages_directory)
    for file in os.listdir():
        my_files_name.append(file)

    start_date = date_to_unix(values.start_date_values)
    end_date = date_to_unix(values.end_date_values)

    my_json = list(map(read_json, my_files_name))
    print(time.ctime(cal.find_the_oldest(my_json) / 1000))

    # all messages
    all_messages = cal.message_count(my_json, start_date, end_date)
    # all reactions
    all_reactions = cal.emoji_all_count(my_json, start_date, end_date)
    # all hearts
    all_hearts = cal.emoji_heart_count(my_json, start_date, end_date)
    # all given reactions
    all_given = cal.giving_reactions(my_json, start_date, end_date)
    # all xD
    all_words = cal.find_word(my_json, start_date, end_date, values.find_word)

    all_emoji = cal.emoji_count(my_json, start_date, end_date)

    printing_dict(all_emoji)
    draw_plot(convert_to_list(all_emoji), "ilość danych emoji")
    # draw all messages plot
    draw_plot(convert_to_list(all_messages), "Ilość wiadomości wysłanych przez osoby")
    # draw all emoji plot
    draw_plot(convert_to_list(all_reactions), "Ilość otrzymanych reakcji pod swoimi wiadomościami")
    # draw all xd plot
    draw_plot(convert_to_list(all_words), "Ilość napisanych '" + values.find_word + "' na konwersacji")
    # draw all hearts plot
    draw_plot(convert_to_list(all_hearts), "Ilość otrzymanych serduszek pod wiadomościami na konwersacji")
    # draw given reactions
    draw_plot(convert_to_list(all_given), "Ilość dawanych reakcji pod wiadomościami")
    # draw emoji ratio
    draw_plot(convert_to_list(cal.ratio(all_reactions, all_messages)),
              "Stosunek ilości otrzymanych reakcji do napisanych wiadomości przez użytkownika")
    # draw heart ratio
    draw_plot(convert_to_list(cal.ratio(all_hearts, all_messages)),
              "Stosunek ilości otrzymanych serduszek do napisanych wiadomości przez użytkownika")
    # draw xd ratio
    draw_plot(convert_to_list(cal.ratio(all_words, all_messages)),
              "Stosunek ilości napisanych '" + values.find_word + "' do napisanych wiadomości przez użytkownika")


# ACTIVATE!
if __name__ == "__main__":
    # IMPORTANT, WRITE YOUR PARAMETERS
    # (<dircetory with messages>, <start date>, <end date>, <Word that you want to find>, <Save graphs>
    values = parameters.Parameters("fixed_messages", [2018, 1, 1], [2022, 3, 1], "xD", False)
    main()
