def find_added(st1, st2):
    string1 = []
    string2 = []
    answer= []
    for i in st1:
        if i not in string1: string1.append(i)
    for i in st2:
        if i not in string2: string2.append(i)
    for letter in string2:
        if letter not in string1:
            count = st2.count(letter)
            for i in range(count):
                answer.append((letter))
        else:
            count1 = st1.count(letter)
            count2 = st2.count(letter)
            if count2 != count1:
                for i in range(count2- count1):
                    answer.append((letter))
    answer.sort()
    answer = "".join(answer)
    return str(answer)
