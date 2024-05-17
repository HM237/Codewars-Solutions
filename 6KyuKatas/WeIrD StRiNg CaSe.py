def to_weird_case(words):
    weirdcase = []
    words = words.split(" ")
    for word in words:
        string =""
        for i in range(0, len(word)):
            if i % 2 ==0: string += (word[i]).upper()
            else: string += (word[i]).lower()
        weirdcase.append(string)
    return " ".join(weirdcase)
