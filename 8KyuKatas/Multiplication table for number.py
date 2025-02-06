def multi_table(number):
    string = ''
    for i in range(1,11):
        if i == 10:
            string = string + (f"{i} * {number} = {i*int(number)}")
        else:
            string = string + (f"{i} * {number} = {i*int(number)}\n")
    return string
