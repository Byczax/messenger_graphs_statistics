from collections import defaultdict
from typing import Callable
from parameters import *

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
    messages = defaultdict(int)
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue

        if any(["photos" in message,
               "gifs" in message,
                "videos" in message,
                "files" in message]):
            messages[message["sender_name"]] += 1
    return messages


# message time in files
def find_time(file: dict, comp: Callable = min) -> int:
    return comp([message["timestamp_ms"] for message in file["messages"]])
