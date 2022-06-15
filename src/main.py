import ast
from inspect import signature
from parameters import *

import time
import os
import sys

from essentials import convert_to_list
from graphs import draw_plot
import calculate as cal
import essentials
import counters as count


def stat_call(data_range: Filepart):

    smaller_functions = [(cal.emoji_all_count,
                          "Liczba otrzymanych reakcji pod swoimi wiadomościami",
                          "Stosunek otrzymanych reakcji do napisanych wiadomości przez użytkownika"),  # emoji count
                         (cal.emoji_heart_count,
                          "Liczba otrzymanych serduszek pod wiadomościami na konwersacji",
                          "Stosunek otrzymanych serduszek do napisanych wiadomości przez użytkownika"),  # heart count
                         (cal.giving_reactions,
                          "Liczba dawanych reakcji pod wiadomościami",
                          "Stosunek dawanych reakcji do napisanych wiadomości przez użytkownika"),  # giving reactions
                         (cal.find_word,
                          "Stosunek napisanych '" + values.find_word + \
                          "' do napisanych wiadomości przez użytkownika",
                          "Stosunek napisanych '" + values.find_word + "' do napisanych wiadomości przez użytkownika")]  # word count

    # all messages
    all_messages = cal.message_count(data_range)

    # draw all messages plot
    draw_plot(convert_to_list(all_messages), "Liczba wiadomości wysłanych przez osoby",
              values.save_graphs, values.path, 1)

    for count, function in zip(range(2, len(smaller_functions)+2), smaller_functions):
        calculate_and_draw(function[0], data_range,
                           function[1], count, all_messages, function[2], len(smaller_functions))


def calculate_and_draw(function, data_range, title, number, all_messages, ratio_title, function_count):
    # calculate
    if len(signature(function).parameters) > 1:
        result = function(data_range, values.find_word)
    else:
        result = function(data_range)

    draw_plot(convert_to_list(result), title,
              values.save_graphs, values.path, number)
    draw_plot(convert_to_list(cal.ratio(result, all_messages)),
              ratio_title, values.save_graphs, values.path, number+function_count)


def count_call(data_range: Filepart):
    count.print_keys(data_range)
    # words = count.count_words(data_range)
    # words = essentials.remove_small(words, 1000)
    # draw_plot(convert_to_list(words), "Liczba napisanych słów",values.save_graphs, values.path,0)


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
    print(sys.argv[1], time.ctime(cal.find_time(new_json) / 1000), len(new_json["messages"]), sep=" | ")
    # print(sys.argv[1], time.ctime(cal.find_time(new_json) / 1000, max), len(new_json["messages"]), sep=" | ")
    data_range = Filepart(new_json, start_date, end_date)
    stat_call(data_range)
    # count_call(data_range)


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
    main()
