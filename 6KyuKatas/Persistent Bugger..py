import numpy
def persistence(n):
    arr =  [int(i) for i in str(n)]
    if len(arr) == 1:
        return 0
    counter = 0
    while len(arr)> 1:
        arr = numpy.prod(arr)
        arr = [int(i) for i in str(arr)]
        counter +=1
    return counter
