def even_numbers(arr,n):
    array = arr[::-1]
    even = []
    index = 0
    count = 0
    while count < n:
        number = array[index]
        if number % 2 ==0:
            count += 1
            even.append(number)
        index += 1
    even = even[::-1]
    return even
