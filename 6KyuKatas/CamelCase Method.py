def camel_case(s):
    s = s.title()
    temp = []
    camel_case = ""
    for i in s.split():
        temp.append(i)
    for i in temp:
        camel_case += i
    return camel_case
