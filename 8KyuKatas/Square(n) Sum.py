def square_sum(numbers):
    temp = []
    for i in numbers:
        i = i ** 2
        temp.append(i)
    return sum(temp)
