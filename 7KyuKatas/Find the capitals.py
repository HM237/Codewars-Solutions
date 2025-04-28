def capitals(word):
    array = []
    position = 0
    for x in word:
        if x.isupper(): array.append(position)
        position += 1
    return array
