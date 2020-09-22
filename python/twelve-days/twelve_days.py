VERSE_START = "On the {ordinal} day of Christmas my true love gave to me:"
VERSE_LAST = "a Partridge in a Pear Tree."

VERSES = {
    2: "two Turtle Doves,",
    3: "three French Hens,",
    4: "four Calling Birds,",
    5: "five Gold Rings,",
    6: "six Geese-a-Laying,",
    7: "seven Swans-a-Swimming,",
    8: "eight Maids-a-Milking,",
    9: "nine Ladies Dancing,",
    10: "ten Lords-a-Leaping,",
    11: "eleven Pipers Piping,",
    12: "twelve Drummers Drumming,",
}

ORDINALS = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}


def create_verse(number):
    verse = [VERSE_START.format(ordinal=ORDINALS[number])]
    verse += [VERSES[n] for n in range(number, 1, -1)]
    if number > 1:
        verse += ["and"]
    verse += [VERSE_LAST]
    return " ".join(verse)


def recite(start_verse, end_verse):
    return [create_verse(n) for n in range(start_verse, end_verse + 1)]
