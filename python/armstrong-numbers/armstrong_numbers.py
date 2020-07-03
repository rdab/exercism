from math import pow
from functools import reduce


def is_armstrong_number(number):
    func = lambda acc, value: acc + pow(int(value), len(str(number)))
    return number == reduce(func, str(number), 0)
