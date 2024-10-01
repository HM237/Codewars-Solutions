def sortme(words):
    dict = {}
    n= 0
    for i in words:
        dict[i] = n
        n+=1
    lowered = []
    values = []
    for i in range(0, len(words)):
        if words[i] != (words[i]).lower():
            lowered.append((words[i]).lower())
            values.append(i)
        else: lowered.append(words[i])
    sortedcase = sorted(lowered)
    uppered = []
    for key,value in dict.items():
        for i in values:
            if i == value:
                uppered.append(key)
    for word in uppered:
        num = (sortedcase.index(word.lower()))
        sortedcase[num] = word
    return sortedcase
