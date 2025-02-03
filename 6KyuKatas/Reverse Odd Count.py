def reverse_odd_count(array):
    indexes = []
    reversedwords = []
    for index in range (0,len(array)):
        word = array[index]
        if array.count(word) % 2 != 0: indexes.append(index)
    opposite = len(indexes) - 1
    for index in indexes:
        newvalue = array[indexes[opposite]]
        reversedwords.append(newvalue)
        opposite -=1    
    for index, reverse in zip(indexes, reversedwords):         
        array[index] = reverse
    return array
