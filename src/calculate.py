from collections import defaultdict
from typing import Callable
from parameters import *
import datetime

# all messages count


def message_count(data: Filepart) -> dict:
    messages = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        messages[message["sender_name"]] += 1
    return messages


# all emoji that people get
def emoji_all_count(data: Filepart) -> dict:
    messages = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if "reactions" not in message:
            continue
        for _ in message["reactions"]:
            messages[message["sender_name"]] += 1
    return messages


# all heart emoji that people get
def emoji_heart_count(data: Filepart) -> dict:
    messages = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if "reactions" not in message:
            continue
        for reaction in message["reactions"]:
            if "\u2764" != reaction["reaction"]:
                continue
            messages[message["sender_name"]] += 1
    return messages


# count all emoji used in conversation
def emoji_count(data: Filepart) -> dict:
    emoji = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if "reactions" not in message:
            continue
        for reaction in message["reactions"]:
            emoji[reaction["reaction"]] += 1
    return emoji


# find how many each people used given word
def find_word(data: Filepart, word: str) -> dict:
    words = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if "content" not in message:
            continue
        words[message["sender_name"]] += message["content"].lower().count(word.lower())
    return words


# how many each user reacted to other messages
def giving_reactions(data: Filepart) -> dict:
    messages = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if "reactions" not in message:
            continue
        for reaction in message["reactions"]:
            messages[reaction["actor"]] += 1
    return messages


# find exact words
def find_only_exact_same(data: Filepart, word: str) -> dict:
    words = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if "content" in message and message["content"] == word:
            words[message["sender_name"]] += 1
    return words


# calculate radio for given parameters
def ratio(all_keys: dict, messages: dict) -> dict:
    ratio = defaultdict(int)
    mul = 10000
    user_names = all_keys.keys()
    for name in user_names:
        if messages[name] and messages[name] >= 100:
            ratio[name] = round(all_keys[name] * mul / messages[name]) / mul
    return ratio


def multimedia(data: Filepart) -> dict:
    messages = {}
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue

        if message["sender_name"] not in messages:
            messages[message["sender_name"]] = {
                "photos": 0,
                "gifs": 0,
                "videos": 0,
                "files": 0,
            }

        if "photos" in message:
            messages[message["sender_name"]]["photos"] += 1
        if "gifs" in message:
            messages[message["sender_name"]]["gifs"] += 1
        if "videos" in message:
            messages[message["sender_name"]]["videos"] += 1
        if "files" in message:
            messages[message["sender_name"]]["files"] += 1

    keys_to_pop = []
    for message in messages:
        if messages[message] == {"photos": 0, "gifs": 0, "videos": 0, "files": 0}:
            keys_to_pop.append(message)
    for key in keys_to_pop:
        messages.pop(key)
    return messages


def unsent_messages(data: Filepart) -> dict:
    messages = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if message["is_unsent"] == True:
            messages[message["sender_name"]] += 1
    return messages


def share_count(data: Filepart) -> dict:
    messages = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if "type" == "Share":
            messages[message["sender_name"]] += 1
    return messages


def sub_unsub_count(data: Filepart) -> dict:
    messages = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if message["sender_name"] not in messages:
            messages[message["sender_name"]] = {
                "subscribe": 0,
                "unsubscribe": 0,
            }
        if "type" == "Subscribe":
            messages[message["sender_name"]]["subscribe"] += 1
        if "type" == "Unsubscribe":
            messages[message["sender_name"]]["unsubscribe"] += 1

    keys_to_pop = []
    for message in messages:
        if messages[message] == {"subscribe": 0, "unsubscribe": 0}:
            keys_to_pop.append(message)
    for key in keys_to_pop:
        messages.pop(key)
    return messages



def message_history(data: Filepart) -> dict:
    counters = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        dt_object = datetime.datetime.fromtimestamp(
            int(message["timestamp_ms"]) / 1000.0
        )
        year = dt_object.year
        month = dt_object.month
        if month < 10:
            month = "0" + str(month)
        week = dt_object.strftime("%U")
        # if int(week) < 10:
        #     week = "0" + str(week)
        combined_date = str(year) + "-" + str(month) + "-" + str(week)
        counters[combined_date] += 1
    return counters


# message time in files
def find_time(file: dict, comp: Callable = min) -> int:
    return comp([message["timestamp_ms"] for message in file["messages"]])
