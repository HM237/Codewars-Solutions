def zeros(n):
    if n < 0 :
        return "dfed"
    count = 0
    while (n >=5 ):
        n //= 5
        count += n
    return count
