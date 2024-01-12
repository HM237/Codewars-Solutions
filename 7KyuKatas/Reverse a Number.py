def reverse_number(n):
    n = str(n)
    if n[0] == "-":
        n = int(n)
        n = abs(n)
        n = str(n)
        n = n[::-1]
        n = int(n)
        return(-n)
    else:
        n = n[::-1]
        return int(n)
