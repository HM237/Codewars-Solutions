def sum_even_numbers(seq): 
    temp = []
    for number in seq:
        if number % 2 == 0:
            temp.append(number)
    return sum(temp)
