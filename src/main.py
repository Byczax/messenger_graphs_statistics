import ast
from parameters import *

import time
import os
import sys

from essentials import convert_to_list
from graphs import draw_plot
import calculate as cal
import essentials


def stat_call(data_range: Filepart):
    # all messages
    all_messages = cal.message_count(data_range)
    # all reactions
    all_reactions = cal.emoji_all_count(data_range)
    # all hearts
    all_hearts = cal.emoji_heart_count(data_range)
    # all given reactions
    all_given = cal.giving_reactions(data_range)
    # all xD
    all_words = cal.find_word(data_range, values.find_word)
    # all gifs, photos
    multimedia = cal.multimedia(data_range)
    # all_emoji = cal.emoji_count(my_json, start_date, end_date)

    # draw all messages plot
    draw_plot(convert_to_list(all_messages), "Liczba wiadomości wysłanych przez osoby",
              values.save_graphs, values.path, 1)
    # draw all emoji plot
    draw_plot(convert_to_list(all_reactions), "Liczba otrzymanych reakcji pod swoimi wiadomościami",
              values.save_graphs, values.path, 2)
    # draw all xd plot
    draw_plot(convert_to_list(all_words), "Liczba napisanych '" + values.find_word +
              "' na konwersacji", values.save_graphs, values.path, 3)
    # draw all hearts plot
    draw_plot(convert_to_list(all_hearts), "Liczba otrzymanych serduszek pod wiadomościami na konwersacji",
              values.save_graphs, values.path, 4)
    # draw given reactions
    draw_plot(convert_to_list(all_given), "Liczba dawanych reakcji pod wiadomościami",
              values.save_graphs, values.path, 5)
    # draw emoji ratio
    draw_plot(convert_to_list(cal.ratio(all_reactions, all_messages)),
              "Stosunek ilości otrzymanych reakcji do napisanych wiadomości przez użytkownika", values.save_graphs, values.path, 6)
    # draw heart ratio
    draw_plot(convert_to_list(cal.ratio(all_hearts, all_messages)),
              "Stosunek ilości otrzymanych serduszek do napisanych wiadomości przez użytkownika", values.save_graphs, values.path, 7)
    # draw xd ratio
    draw_plot(convert_to_list(cal.ratio(all_words, all_messages)),
              "Stosunek ilości napisanych '" + values.find_word +
              "' do napisanych wiadomości przez użytkownika",
              values.save_graphs, values.path, 8)


# main function
def main():
    # * Get data from files
    my_files_name = []
    os.chdir(values.messages_directory)
    for file in os.listdir():
        if file.endswith(".json"):
            my_files_name.append(file)
    my_json = list(map(essentials.read_json, my_files_name))
    os.chdir("..")  # Exit from folder with messages

    # * Remove duplicates
    users = set()
    messages = set()
    for file in my_json:
        for message in file["messages"]:
            messages.add(str(message))
    for user in file["participants"]:
        users.add(str(user))
    new_json = {}
    new_json["messages"] = [ast.literal_eval(message) for message in messages]
    new_json["users"] = [ast.literal_eval(user) for user in users]

    # Convert given dates to unix
    start_date = essentials.date_to_unix(values.start_date_values)
    end_date = essentials.date_to_unix(values.end_date_values)

    # print()
    print(sys.argv[1], time.ctime(cal.find_time(
        new_json) / 1000), len(new_json["messages"]), sep=" | ")
    # print(sys.argv[1], time.ctime(cal.find_time(
    #     new_json) / 1000, max), len(new_json["messages"]), sep=" | ")
    data_range = Filepart(new_json, start_date, end_date)
    stat_call(data_range)


def read_args():
    if len(sys.argv) < 5 or sys.argv[1][0] == '-':
        print("Usage:" + sys.argv[
            0] + " <file(s) path> <start date([yyyy, mm, dd])> <end date([yyyy, mm, dd])> <word to find> <save image(boolean: True|False)> <save path>")
    else:
        files = sys.argv[1]
        start_date = [int(i) for i in sys.argv[2][1:-1].split(",")]
        end_date = [int(i) for i in sys.argv[3][1:-1].split(",")]
        word = sys.argv[4]
        save = bool(sys.argv[5])
        path = sys.argv[6]
        print(path)
        return Parameters(files, start_date, end_date, word, save, path)


# ACTIVATE!
if __name__ == "__main__":
    values = read_args()
    # IMPORTANT, WRITE YOUR PARAMETERS
    # (<directory with messages>, <start date>, <end date>, <Word that you want to find>, <Save graphs>
    # values = parameters.Parameters("fixed_messages", [2017, 10, 1], [2022, 3, 1], "xD", False)  # all
    # values = parameters.Parameters("fixed_messages", [2019, 10, 1], [2020, 2, 28], "xD", True)  # 3 semestr 2018
    # values = parameters.Parameters("fixed_messages", [2020, 10, 1], [2021, 2, 28], "xD", True)  # 5 semestr 2018
    # values = parameters.Parameters("fixed_messages", [2019, 3, 1], [2019, 7, 1], "xD", True)  # 2 semestr 2018
    # values = parameters.Parameters("fixed_messages", [2020, 3, 1], [2020, 7, 1], "xD", True)  # 4 semestr 2018
    # values = parameters.Parameters("fixed_messages", [2021, 3, 1], [2021, 7, 1], "xD", True)  # 6 semestr 2018
    main()
