def solution(array_a, array_b):
    temp = []
    diff = 0
    average = 0
    for a,b in zip (array_a, array_b):
        diff = (b-a)**2
        temp.append(diff)
    average = sum(temp) / int(len(array_a))
    return average
