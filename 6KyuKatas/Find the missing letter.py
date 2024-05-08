def find_missing_letter(chars):
    if chars[0] == (chars[0]).upper():
        array = []
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        start_letter = alphabet.index(chars[0])
        last_letter = alphabet.index(chars[-1])
        for i in range (start_letter, last_letter + 1):
            array.append(alphabet[i])
        for a,b in zip(array, chars): 
            if a != b : return a
    else:
        array = []
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        start_letter = alphabet.index(chars[0])
        last_letter = alphabet.index(chars[-1])
        for i in range (start_letter, last_letter + 1):
            array.append(alphabet[i])
        for a,b in zip(array, chars): 
            if a != b : return a
