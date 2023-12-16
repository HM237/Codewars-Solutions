def repeats(arr):
    temp = []
    for i in arr:
        if arr.count(i) == 1:
            temp.append(i)
    return sum(temp)
