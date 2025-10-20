from collections import Counter
from .utils import clean_text

def word_count(text: str) -> int:
    return len(clean_text(text).split())

def char_count(text: str) -> int:
    return len(text)

def most_common_words(text: str, n: int = 3):
    words = clean_text(text).split()
    return Counter(words).most_common(n)
