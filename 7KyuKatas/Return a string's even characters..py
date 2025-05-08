def even_chars(string): 
    even_characters = []
    if len(string) < 2  or len(string) > 100:
        return "invalid string"
    else:
        for index, character in enumerate(string):
            if index % 2 != 0 : even_characters.append(character)
    return (even_characters)
