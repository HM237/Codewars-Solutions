def up_array(arr):
    number = []
    string = ""
    if len(arr) == 0: return None
    for i in arr:
        if len(str(i)) > 1 or abs(i) != i: return None
        else:
            string += str(i)
    for i in string:
        if i == "0":
            number.append(0)
        else:
            break
    string = str(int(string) + 1)
    for i in string:
        number.append(int(i))
    if string == "1": return [1]
    return number
