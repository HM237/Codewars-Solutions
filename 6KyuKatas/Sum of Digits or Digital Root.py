def digital_root(n):
    array = [int(i) for i in str(n)]
    if len(array) == 1:
        return n
    while len(array) > 1:
        array = sum(array)
        array = [int(i) for i in str(array)]
        n = array[0]   
    return n
