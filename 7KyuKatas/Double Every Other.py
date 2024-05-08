def double_every_other(lst):
    array = []
    for index in range(len(lst)):
        if index % 2 == 0: array.append(lst[index])
        else: array.append((lst[index]) * 2)
    return array
