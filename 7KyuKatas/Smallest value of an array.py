def find_smallest(numbers, to_return):
    if to_return == "value":
        return min(numbers)
    else:
        a = min(numbers)
        for i in numbers:
            if i == a:
                return numbers.index(i)
