import parameters

import time
import os

from src.essentials import convert_to_list
from src.graphs import draw_plot
from src import calculate as cal
from src import essentials


# main function
def main():
    my_files_name = []
    os.chdir("../" + values.messages_directory)
    for file in os.listdir():
        my_files_name.append(file)

    start_date = essentials.date_to_unix(values.start_date_values)
    end_date = essentials.date_to_unix(values.end_date_values)

    my_json = list(map(essentials.read_json, my_files_name))
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

    # all_emoji = cal.emoji_count(my_json, start_date, end_date)

    # essentials.printing_dict(all_emoji)
    # draw_plot(convert_to_list(all_emoji), "ilość danych emoji")

    # draw all messages plot
    draw_plot(convert_to_list(all_messages), "Ilość wiadomości wysłanych przez osoby", values.save_graphs)
    # draw all emoji plot
    draw_plot(convert_to_list(all_reactions), "Ilość otrzymanych reakcji pod swoimi wiadomościami", values.save_graphs)
    # draw all xd plot
    draw_plot(convert_to_list(all_words), "Ilość napisanych '" + values.find_word + "' na konwersacji",
              values.save_graphs)
    # draw all hearts plot
    draw_plot(convert_to_list(all_hearts), "Ilość otrzymanych serduszek pod wiadomościami na konwersacji",
              values.save_graphs)
    # draw given reactions
    draw_plot(convert_to_list(all_given), "Ilość dawanych reakcji pod wiadomościami", values.save_graphs)
    # draw emoji ratio
    draw_plot(convert_to_list(cal.ratio(all_reactions, all_messages)),
              "Stosunek ilości otrzymanych reakcji do napisanych wiadomości przez użytkownika", values.save_graphs)
    # draw heart ratio
    draw_plot(convert_to_list(cal.ratio(all_hearts, all_messages)),
              "Stosunek ilości otrzymanych serduszek do napisanych wiadomości przez użytkownika", values.save_graphs)
    # draw xd ratio
    draw_plot(convert_to_list(cal.ratio(all_words, all_messages)),
              "Stosunek ilości napisanych '" + values.find_word + "' do napisanych wiadomości przez użytkownika",
              values.save_graphs)


# ACTIVATE!
if __name__ == "__main__":
    # IMPORTANT, WRITE YOUR PARAMETERS
    # (<directory with messages>, <start date>, <end date>, <Word that you want to find>, <Save graphs>
    values = parameters.Parameters("fixed_messages", [2018, 10, 1], [2022, 3, 1], "xD", False)
    main()
