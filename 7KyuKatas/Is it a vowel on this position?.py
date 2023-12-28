def check_vowel(string, position):
    if len(string) < position or position < 0: return False
    letter = string[position]
    letter = letter.lower()
    if letter in "aeiou": return True
    else: return False
