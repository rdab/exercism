import re
pattern = "^\d{9}[\dX]$"

def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if re.match(pattern, isbn) is None:
        return False
    if isbn[-1] == 'X':
        isbn = list(isbn)[:9] + [10]
    return sum(map(lambda x,y: int(x)*y, isbn, range(10, 0, -1))) % 11 == 0
