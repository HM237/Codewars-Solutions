def to_camel_case(text):
    arr = []
    temp = []
    delimiters = [ "-", "_"]
    for delimiter in delimiters:
        text = " ".join(text.split(delimiter))
    text = text.split(" ")
    for i in text:
        temp.append(i)
    arr.append(temp[0])
    for i in temp:
        if i != arr[0]:
            a = i.title()
            arr.append(a)
    arr= "".join(arr)
    return arr
