def do_math(s) :
    numbers = []
    letters = []
    ordered_numbers = []
    s = s.split(" ")
    for string in s:
        for character in string:
            if character in "abcefghijklmnopqrstuvwxyz":
                letters.append(character)
                number = string.replace(character, "")
                numbers.append(number)
    list1 = list(enumerate(letters))
    list2 = sorted(list1, key = lambda x:x[1])
    for index,letter in list2:
        ordered_numbers.append(numbers[index])
    for i in range(len(ordered_numbers)):
        string = ""
        string += ordered_numbers[i]
    #TRIAL NTO COMPLETED
