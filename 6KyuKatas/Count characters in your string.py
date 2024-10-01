def count(s):
    characters = []
    count = []
    dict = {}
    for character in s:
        if character not in characters: characters.append(character)
    for character in characters: count.append(s.count(character))
    for a,b in zip(characters, count):
        dict[a] = b
    return(dict)
