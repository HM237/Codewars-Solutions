def remainder(a,b):
    c= 0
    if a == 0 and a > b:
        return 0
    elif a == 0 and b == 0:
        return None
    elif b == 0 and b > a:
        return 0
    elif a== 0 and a < b:
        return None
    elif b == 0 and b < a:
        return None
    elif a > b:
        c = a % b
    elif a < b:
        c = b % a
    return c
