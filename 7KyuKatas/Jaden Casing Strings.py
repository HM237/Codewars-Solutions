def to_jaden_case(string):
    temp = []
    string = string.split()
    for i in string:
        i = i.capitalize()
        temp.append(i)
    return " ".join(temp)
