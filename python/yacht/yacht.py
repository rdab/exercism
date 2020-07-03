"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

from collections import Counter

def sum_number(dice, number):
    return number * dice.count(number)

def calc_four(dice):
    val, count = Counter(dice).most_common(1)[0]
    return val*4 if count >= 4 else 0

d = {
    YACHT: (lambda dice: 50 if len(set(dice)) == 1 else 0),
    ONES: (lambda dice: sum_number(dice, 1)),
    TWOS: (lambda dice: sum_number(dice, 2)),
    THREES: (lambda dice: sum_number(dice, 3)),
    FOURS: (lambda dice: sum_number(dice, 4)),
    FIVES: (lambda dice: sum_number(dice, 5)),
    SIXES: (lambda dice: sum_number(dice, 6)),
    FULL_HOUSE: (lambda dice: sum(dice) if sorted(Counter(dice).values()) == [2, 3] else 0),
    FOUR_OF_A_KIND: calc_four,
    LITTLE_STRAIGHT: (lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0),
    BIG_STRAIGHT: (lambda dice: 30 if sorted(dice) == [2,3,4,5,6] else 0),
    CHOICE: sum
}

def score(dice, category):
    return d.get(category)(dice)
