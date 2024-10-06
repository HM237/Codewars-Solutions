def descending_order(num):
    numbers = []
    for i in str(num): numbers.append(int(i))
    numbers.sort(reverse= True)
    reversed = []
    for number in numbers: reversed.append(str(number))
    return int("".join(reversed))
