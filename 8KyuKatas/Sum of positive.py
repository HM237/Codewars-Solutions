def positive_sum(arr):
    newarr= []
    if arr == []:
        return 0
    for i in arr:
        if i > 0:
            newarr.append(i)
    x = sum(newarr)
    return x
