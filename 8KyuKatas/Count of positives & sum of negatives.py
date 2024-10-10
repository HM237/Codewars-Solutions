def count_positives_sum_negatives(arr):
    if arr == [0,0,0,0,0,0,0,0,0] : return [0,0]
    positive = []
    negative = []
    for number in arr:
        if number > 0: positive.append(number)
        elif number < 0: negative.append(number)
    if [(len(positive)),(sum(negative))] == [0,0]: return []
    else: return [(len(positive)),(sum(negative))]
