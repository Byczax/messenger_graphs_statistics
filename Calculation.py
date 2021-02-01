import json

import matplotlib.pyplot as plt


def read_json(filename: str):
    with open(filename) as file:
        data = json.load(file)
        return data


def message_count(my_files):
    my_messages = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if message["sender_name"] not in my_messages:
                my_messages[message["sender_name"]] = 1
            else:
                my_messages[message["sender_name"]] += 1
    return my_messages


def emoji_all_count(my_files):
    my_messages = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if "reactions" in message:
                for reaction in message["reactions"]:
                    if message["sender_name"] not in my_messages:
                        my_messages[message["sender_name"]] = 0
                    my_messages[message["sender_name"]] += 1
    return my_messages


def emoji_heart_count(my_files):
    my_messages = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if "reactions" in message:
                for reaction in message["reactions"]:
                    if "\u2764" == reaction["reaction"]:
                        if message["sender_name"] not in my_messages:
                            my_messages[message["sender_name"]] = 0
                        my_messages[message["sender_name"]] += 1
    return my_messages


def find_the_oldest(my_files):
    timestamps = []
    for my_file in my_files:
        for message in my_file["messages"]:
            timestamps.append(message["timestamp_ms"])
    return min(timestamps)


def printing_dict(messages):
    for user in messages:
        print(user)


def find_XD(my_files):
    my_xd = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if "content" in message:
                xd_count = message["content"].lower().count("xd")
                if xd_count > 0:
                    if message["sender_name"] not in my_xd:
                        my_xd[message["sender_name"]] = xd_count
                    else:
                        my_xd[message["sender_name"]] += xd_count
    return my_xd


def giving_reactions(my_files):
    my_messages = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if "reactions" in message:
                for reaction in message["reactions"]:
                    if reaction["actor"] not in my_messages:
                        my_messages[reaction["actor"]] = 0
                    my_messages[reaction["actor"]] += 1
    return my_messages


def draw_plot(data, plot_name):
    plt.rcParams.update({'font.size': 8})
    plt.figure(num=None, figsize=(20, 8), dpi=400, facecolor='w', edgecolor='k')
    plt.bar(list(map(lambda my_tuple: my_tuple[0], data)),
            list(map(lambda my_tuple: my_tuple[1], data)))
    for caption in data:
        plt.text(caption[0], caption[1], caption[1], rotation=90, va='bottom', ha='center')
    plt.xticks(rotation=90)
    plt.title(plot_name)
    plt.show()


def export_to_csv(messages, filename):
    with open(filename, 'w', encoding="utf-8") as my_file:
        my_file.write("Username" + ";" + "messages" + "\n")
        for output in messages:
            my_file.write(output[0] + ";" + str(output[1]) + "\n")


def ratio(all_keys, my_messages):
    my_ratio = {}
    user_names = all_keys.keys()
    for name in user_names:
        if my_messages[name] >= 100:
            my_ratio[name] = round(all_keys[name] * 10000 / my_messages[name]) / 10000
    return my_ratio


def convert_to_list(data):
    my_return = list(data.items())
    my_return.sort(key=lambda my_tuple: my_tuple[1])
    return my_return


def main():
    my_files_name = ["./message_1_fixed.json", "./message_2_fixed.json", "./message_3_fixed.json"]
    my_json = list(map(read_json, my_files_name))
    # all messages
    all_messages = message_count(my_json)
    # all reactions
    all_reactions = emoji_all_count(my_json)
    # all hearts
    all_hearts = emoji_heart_count(my_json)
    # all given reactions
    all_given = giving_reactions(my_json)
    # all xD
    all_xd = find_XD(my_json)
    # draw all messages plot
    draw_plot(convert_to_list(all_messages), "Ilość wiadomości wysłanych przez osoby")
    # draw all emoji plot
    draw_plot(convert_to_list(all_reactions), "Ilość otrzymanych reakcji pod swoimi wiadomościami")
    # draw all xd plot
    draw_plot(convert_to_list(all_xd), "Ilość napisanych 'xD' na konwersacji")
    # draw all hearts plot
    draw_plot(convert_to_list(all_hearts), "Ilość otrzymanych serduszek pod wiadomościami na konwersacji")
    # draw given reactions
    draw_plot(convert_to_list(all_given), "Ilość dawanych reakcji pod wiadomościami")
    # draw emoji ratio
    draw_plot(convert_to_list(ratio(all_reactions, all_messages)),
              "Stosunek ilości otrzymanych reakcji do napisanych wiadomości przez użytkownika")
    # draw xd ratio
    draw_plot(convert_to_list(ratio(all_hearts, all_messages)),
              "Stosunek ilości otrzymanych serduszek do napisanych wiadomości przez użytkownika")
    # draw xd ratio
    draw_plot(convert_to_list(ratio(all_xd, all_messages)),
              "Stosunek ilości napisanych 'xD' do napisanych wiadomości przez użytkownika")


if __name__ == "__main__":
    main()
