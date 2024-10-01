def data_reverse(data):
    reversed = []
    start = 0
    end = len(data)
    step = 8
    for i in range(start, end, step):
        x = i
        reversed.insert(0,(data[x:x+step]))
    reversed_data = []
    for array in reversed:
        for i in array:
            reversed_data.append(i)
    return reversed_data
