def generate_hashtag(s):
    s = s.title()
    temp = []
    camel_case = ""
    if s == "":
        return False
    for i in s.split():
        temp.append(i)
    for i in temp:
        camel_case += i
    b = "#"
    b= b + camel_case
    if len(b) > 140:
        return False
    return b
