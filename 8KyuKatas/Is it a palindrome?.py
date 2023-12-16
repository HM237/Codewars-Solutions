def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False
