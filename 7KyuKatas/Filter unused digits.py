def unused_digits(*numbers):
    numbers = "".join(str(x) for x in numbers)
    un_used = []
    for digit in list('0123456789'):
        if numbers.count(digit) == 0:
            un_used.append(digit)
    return ''.join(un_used)
