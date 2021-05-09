import string


# all messages count
def message_count(my_files: list, start_date: int, end_date: int) -> dict:
    my_messages = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if end_date >= message["timestamp_ms"] >= start_date:
                if message["sender_name"] not in my_messages:
                    my_messages[message["sender_name"]] = 0
                my_messages[message["sender_name"]] += 1
    return my_messages


# all emoji that people get
def emoji_all_count(my_files: list, start_date: int, end_date: int) -> dict:
    my_messages = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if "reactions" in message:
                for _ in message["reactions"]:
                    if end_date >= message["timestamp_ms"] >= start_date:
                        if message["sender_name"] not in my_messages:
                            my_messages[message["sender_name"]] = 0
                        my_messages[message["sender_name"]] += 1
    return my_messages


# all heart emoji that people get
def emoji_heart_count(my_files: list, start_date: int, end_date: int) -> dict:
    my_messages = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if "reactions" in message:
                for reaction in message["reactions"]:
                    if "\u2764" == reaction["reaction"]:
                        if end_date >= message["timestamp_ms"] >= start_date:
                            if message["sender_name"] not in my_messages:
                                my_messages[message["sender_name"]] = 0
                            my_messages[message["sender_name"]] += 1
    return my_messages


# count all emoji used in conversation
def emoji_count(my_files: list, start_date: int, end_date: int) -> dict:
    emoji = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if "reactions" in message:
                for reaction in message["reactions"]:
                    if end_date >= message["timestamp_ms"] >= start_date:
                        if reaction["reaction"] not in emoji:
                            emoji[reaction["reaction"]] = 0
                        emoji[reaction["reaction"]] += 1
    return emoji


# find how many each people used given word
def find_word(my_files: list, start_date: int, end_date: int, word: string) -> dict:
    my_words = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if "content" in message:
                word_count = message["content"].lower().count(word.lower())
                if word_count > 0:
                    if end_date >= message["timestamp_ms"] >= start_date:
                        if message["sender_name"] not in my_words:
                            my_words[message["sender_name"]] = 0
                        my_words[message["sender_name"]] += word_count
    return my_words


# how many each user reacted to other messages
def giving_reactions(my_files: list, start_date: int, end_date: int) -> dict:
    my_messages = {}
    for my_file in my_files:
        for message in my_file["messages"]:
            if "reactions" in message:
                for reaction in message["reactions"]:
                    if end_date >= message["timestamp_ms"] >= start_date:
                        if reaction["actor"] not in my_messages:
                            my_messages[reaction["actor"]] = 0
                        my_messages[reaction["actor"]] += 1
    return my_messages


# calculate radio for given parameters
def ratio(all_keys: dict, my_messages: dict) -> dict:
    my_ratio = {}
    user_names = all_keys.keys()
    for name in user_names:
        if my_messages[name] and my_messages[name] >= 100:
            my_ratio[name] = round(all_keys[name] * 10000 / my_messages[name]) / 10000
    return my_ratio


# oldest message in files
def find_the_oldest(my_files: list) -> int:
    timestamps = []
    for my_file in my_files:
        for message in my_file["messages"]:
            timestamps.append(message["timestamp_ms"])
    return min(timestamps)
