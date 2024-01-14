def digitize(n):
    digitised = []
    list1 = list(str(n))
    for i in list1: digitised.append(int(i))
    return digitised


#OR


def digitize(n):
    digitised = [int(i) for i in str(n)]
    return digitised
