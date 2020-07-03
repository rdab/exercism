def find_anagrams(word, candidates):
    word = word.lower()
    return [
        item
        for item in candidates
        if word != item.lower() and sorted(word) == sorted(item.lower())
    ]
