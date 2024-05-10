def find_short(s):
    array = s.split(" ")
    lengths = []
    for word in array: lengths.append(len(word))
    return min(lengths)



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
