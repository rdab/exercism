import re
from collections import Counter


def count_words(sentence):
    sentence = sentence.lower().replace('_', ' ')
    return Counter(re.findall(r"\w+(?:'\w+)?", sentence))
