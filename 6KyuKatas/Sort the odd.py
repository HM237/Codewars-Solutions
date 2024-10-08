def sort_array(source_array):
    odds = []
    n = 0
    for number in source_array:
        if number % 2 != 0 : odds.append(number)
    for i in range( 0 , len(source_array)):
        if source_array[i] % 2 != 0 :
            source_array[i] = sorted(odds)[n]
            n += 1
    return source_array
