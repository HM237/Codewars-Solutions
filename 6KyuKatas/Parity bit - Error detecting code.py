def parity_bit(binary):
    array = binary.split(" ")
    new_array = []
    for i in array:
        x = i.count("1")
        if x % 2 != 0 : new_array.append("error")
        else: new_array.append(i[0:7])
    return " ".join(new_array)
