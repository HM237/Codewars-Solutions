def neutralise(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    str = ""
    for a,b in zip(list1, list2):
        if a =="+" and b == "+": str+="+"
        elif a== "-" and b == "-": str+= "-"
        else: str+= "0"
    return str
