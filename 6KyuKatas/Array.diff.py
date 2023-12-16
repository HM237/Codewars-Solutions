def array_diff(a, b):
    temp = []
    for i in a:
        if i not in b:
            temp.append(i)
    return temp   



#OR


def array_diff(a, b):
    temp = []
    disregard= []
    for i in a:
        if i in b:
            disregard.append(i)
        else:
            temp.append(i)
    return temp        
