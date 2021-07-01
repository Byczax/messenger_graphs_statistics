import string
from dataclasses import dataclass
from typing import List

@dataclass
class Parameters:
    messages_directory: string
    start_date_values: List[int]
    end_date_values: List[int]
    find_word: string
    save_graphs: bool
    path: str
