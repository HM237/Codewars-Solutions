def find_average(numbers):
    if numbers == []:
        return 0
    length = len(numbers)
    x = sum(numbers)
    return x / length
