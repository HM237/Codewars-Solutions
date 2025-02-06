def is_isogram(string):
    string = string.lower()
    for character in string:
        if string.count(character) > 1: return False
    return True
