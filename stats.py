from collections import Counter
from typing import Dict, List

def count_words(text: str) -> int:
    word_count = len(text.split())
    return word_count

def count_chars(text: str, case_sensitive: bool = False) -> Counter:
    return Counter(text if case_sensitive else text.lower())

def get_alphabetic_char_counts(text: str, case_sensitive: bool = False) -> List[Dict[str, int]]:
    char_counter = count_chars(text, case_sensitive)

    return [
        {"char": char, "count": count}
        for char, count in char_counter.most_common()
        if char.isalpha()
    ]
