from string import ascii_lowercase


def is_isogram(string):
    string = [letter for letter in string.lower() if letter in ascii_lowercase]
    return len(string) == len(set(string))
