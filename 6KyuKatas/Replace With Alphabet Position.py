def alphabet_position(text):
    text = text.lower()
    list1 = list(text)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    positions = []
    for letter in list1: 
        if letter in alphabet: positions.append(str((alphabet.index(letter)) + 1))
    return( " ".join(positions))
