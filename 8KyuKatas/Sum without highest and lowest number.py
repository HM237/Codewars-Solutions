def sum_array(arr):
    answer = []
    if arr == [] or arr == None: return 0
    else:
        arr = sorted(arr)
        for i in range(1, len(arr)-1): answer.append(arr[i])
    return sum(answer)
