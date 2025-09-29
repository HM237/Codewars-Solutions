def digitize(n):
    arr = []
    for number in str(n):
        arr.append(int(number))
    return arr[::-1]
