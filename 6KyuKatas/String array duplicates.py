def dup(arry):
    removed = []
    for word in arry:
        temp = []
        for character in word:
            if character not in temp:
                temp.append(character)
            else:
                if temp[-1] != character:
                    temp.append(character)
        temp = "".join(temp)
        removed.append(temp)
    return removed
