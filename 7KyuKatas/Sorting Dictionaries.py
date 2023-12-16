def sort_dict(d):
    sorted = []
    temp = []
    for value in d.values():
        temp.append(value)
    temp.sort(reverse = True)
    for i in temp:
        for key, value in d.items():
            if value == i :
                sorted.append((key,i))
    return sorted
