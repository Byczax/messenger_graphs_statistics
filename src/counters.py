from collections import defaultdict
from typing import Callable
from parameters import *


def count_words(data: Filepart) -> dict:
    words = defaultdict(int)
    for message in data.file["messages"]:
        if 'content' not in message:
            continue
        if message["type"] != "Generic":
            continue
        for word in message["content"].split():
            words[word.lower()] += 1
    return words


def print_keys(data: Filepart):
    keys = set()

    print(data.file.keys())
    for message in data.file["messages"]:
        for key in message.keys():
            keys.add(key)
    print(keys)
