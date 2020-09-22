VERSE_START = "On the {ordinal} day of Christmas my true love gave to me:"

d = {
    1: "a Partridge in a Pear Tree.",
    2: "two Turtle Doves, ",
    3: "three French Hens, ",
}

ORDINALS = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth"}

verses = [
    ("first", "a Partridge in a Pear Tree."),
    ("second", "two Turtle Doves,"),
    ("third", "three French Hens,"),
    ("fourth", "four Calling Birds,"),
]


def recite(start_verse, end_verse):
    result = [VERSE_START.format(ordinal=verses[start_verse-1][0])]
    v = [verses[n-1][1] for n in range(end_verse, 1, -1)]
    result += v
    if end_verse > 1:
        result += ['and']
    result += [verses[0][1]]
    return [' '.join(result)]
