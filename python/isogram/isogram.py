from string import ascii_lowercase

def is_isogram(string):
    s = [l for l in string.lower() if l in ascii_lowercase]
    return len(s) == len(set(s))
