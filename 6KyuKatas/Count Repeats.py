def count_repeats(txt):
    i = 0
    j = 0
    count=  -1
    new = ""
    while (j < len(txt)):
        if (txt[i] == txt[j]):
            j += 1
            count += 1
        else:
            i = j
            j += 1
    return count
