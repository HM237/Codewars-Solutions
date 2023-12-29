def duplicate_count(text):
    text = text.lower()
    temp = []
    count = []
    answer = 0
    for i in text:
        a = i.lower()
        if a not in temp: temp.append(a)
    for i in temp:
        counter = text.count(i)
        count.append(counter)
    for i in count: if i > 1: answer+=1
    return answer
