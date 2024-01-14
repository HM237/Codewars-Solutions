def solution(s):
    string = ""
    for i in s:
        if i != i.upper():
            string += i
        else:
            string += " "
            string += i
    return(string)
