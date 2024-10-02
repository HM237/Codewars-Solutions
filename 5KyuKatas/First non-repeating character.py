def first_non_repeating_letter(s):#
    for character in s:
        if s.lower().count(character.lower()) == 1: return character
    return ""
