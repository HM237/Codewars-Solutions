def spin_words(sentence):
    temp = []
    for i in sentence.split():
        if len(i) >= 5:
            temp.append(i[::-1])
        else:
            temp.append(i)
    return ' '.join(temp)
