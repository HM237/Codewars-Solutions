def solve(arr):
    numbers = []
    frequency = []
    answer = []
    for i in arr:
        if i not in numbers: numbers.append(i)
    numbers.sort()
    for i in numbers:
        count = arr.count(i)
        frequency.append(count)
    list1 = list(enumerate(frequency))
    list2 = sorted(list1, key=lambda x:x[1], reverse = True)
    for index,value in list2:
        number = numbers[index]
        for i in range(value):
            answer.append(number)
    return(answer)
