def find_short(s):
    s= s.split()
    temp = []
    for i in s:
        temp.append(len(i))
    return min(temp)




#OR


def find_short(s):
    s = s.split()
    words = []
    lengths = []
    for i in s:
        words.append(i)
    lengths = []
    for i in s:
        lengths.append(len(i))
    shortest = min(lengths)
    return shortest
