def expanded_form(num):
    length = len(str(num))
    power = length
    array = []
    for i in range(0,length):
        number = int(str(num)[i]) *  (10**(power-1))
        array.append(number)
        power -= 1
    expanded = f'{array[0]} '
    for i in range(1,length):
        if array[i] != 0 : expanded += f'+ {array[i]} '
    return(expanded[:(len(expanded)-1)])
