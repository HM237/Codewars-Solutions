def is_pangram(s):
    s = s.lower()
    letters = list("abcdefghijklmnopqrstuvwxyz")
    checker = []
    for letter in letters:
        if s.count(letter) >= 1:
            checker.append(True)
        else: checker.append(False)
    if False in checker: return False
    else: return True
