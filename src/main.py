import parameters

import time
import os
import sys

from essentials import convert_to_list
from graphs import draw_plot
import calculate as cal
import essentials


def stat_call(my_json: list, start_date: int, end_date: int):
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

    # all_emoji = cal.emoji_count(my_json, start_date, end_date)

    # # essentials.printing_dict(all_emoji)
    # draw_plot(convert_to_list(all_emoji), "ilość danych emoji", values.save_graphs, 0)

    # draw all messages plot
    draw_plot(convert_to_list(all_messages), "Ilość wiadomości wysłanych przez osoby", values.save_graphs, 1,
              values.path)
    # draw all emoji plot
    draw_plot(convert_to_list(all_reactions), "Ilość otrzymanych reakcji pod swoimi wiadomościami", values.save_graphs,
              2, values.path)
    # draw all xd plot
    draw_plot(convert_to_list(all_words), "Ilość napisanych '" + values.find_word + "' na konwersacji",
              values.save_graphs, 3, values.path)
    # draw all hearts plot
    draw_plot(convert_to_list(all_hearts), "Ilość otrzymanych serduszek pod wiadomościami na konwersacji",
              values.save_graphs, 4, values.path)
    # draw given reactions
    draw_plot(convert_to_list(all_given), "Ilość dawanych reakcji pod wiadomościami", values.save_graphs, 5,
              values.path)
    # draw emoji ratio
    draw_plot(convert_to_list(cal.ratio(all_reactions, all_messages)),
              "Stosunek ilości otrzymanych reakcji do napisanych wiadomości przez użytkownika", values.save_graphs, 6,
              values.path)
    # draw heart ratio
    draw_plot(convert_to_list(cal.ratio(all_hearts, all_messages)),
              "Stosunek ilości otrzymanych serduszek do napisanych wiadomości przez użytkownika", values.save_graphs, 7,
              values.path)
    # draw xd ratio
    draw_plot(convert_to_list(cal.ratio(all_words, all_messages)),
              "Stosunek ilości napisanych '" + values.find_word + "' do napisanych wiadomości przez użytkownika",
              values.save_graphs, 8, values.path)


# main function
def main():
    my_files_name = []
    # my_files_name = [file for file in os.listdir("../" + values.messages_directory)]
    os.chdir(values.messages_directory)
    for file in os.listdir():
        my_files_name.append(file)
    my_json = list(map(essentials.read_json, my_files_name))
    os.chdir("..")
    # os.chdir("..")
    start_date = essentials.date_to_unix(values.start_date_values)
    end_date = essentials.date_to_unix(values.end_date_values)

    
    print(time.ctime(cal.find_the_oldest(my_json) / 1000))
    stat_call(my_json, start_date, end_date)


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
        return parameters.Parameters(files, start_date, end_date, word, save, path)


# ACTIVATE!
if __name__ == "__main__":
    values = read_args()
    # IMPORTANT, WRITE YOUR PARAMETERS
    # (<directory with messages>, <start date>, <end date>, <Word that you want to find>, <Save graphs>
    # values = parameters.Parameters("fixed_messages", [2017, 10, 1], [2022, 3, 1], "xD", False)  # all
    # values = parameters.Parameters("./fixed_messages/2019", [2020, 10, 1], [2021, 2, 28], "xD", True, "../img/samorzad/zima-2020/")  # 1 semestr 2018
    # values = parameters.Parameters("fixed_messages", [2019, 10, 1], [2020, 2, 28], "xD", True)  # 3 semestr 2018
    # values = parameters.Parameters("fixed_messages", [2020, 10, 1], [2021, 2, 28], "xD", True)  # 5 semestr 2018
    # values = parameters.Parameters("fixed_messages", [2019, 3, 1], [2019, 7, 1], "xD", True)  # 2 semestr 2018
    # values = parameters.Parameters("fixed_messages", [2020, 3, 1], [2020, 7, 1], "xD", True)  # 4 semestr 2018
    # values = parameters.Parameters("fixed_messages", [2021, 3, 1], [2021, 7, 1], "xD", True)  # 6 semestr 2018
    main()
