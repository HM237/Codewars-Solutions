def multiply(n):
    power = (len(str(n)))
    if str(n)[0]== "-":
        n = abs(n)
        power = len(str(n))
        return(-(n*(5**power)))
    return n * (5**power)
