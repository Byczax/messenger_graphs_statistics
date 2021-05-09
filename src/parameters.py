import string
from dataclasses import dataclass


@dataclass
class Parameters:
    messages_directory: string
    start_date_values: list[int]
    end_date_values: list[int]
    find_word: string
    save_graphs: bool
