def move_zeros(lst):
    temp = []
    count = lst.count(0)
    for i in lst:
        if i != 0 :
            temp.append(i)
    for i in range(count):
        temp.append(0)
    return temp
