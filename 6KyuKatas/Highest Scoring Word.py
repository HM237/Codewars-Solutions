def high(x):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    list1 = x.split(" ")
    score = []
    for word in list1:
        value = 0
        for letter in word:
            point = alphabet.index(letter)
            value += point + 1
        score.append(value)
    return list1[score.index(max(score))]
