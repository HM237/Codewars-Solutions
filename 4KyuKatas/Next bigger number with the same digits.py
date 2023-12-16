def next_bigger(num):
    numlist = [int(i) for i in str(num)]

    index_of_replace_num = -1
    i = len(numlist) - 1
    while i > 0:
        if numlist[i] > numlist[i-1]:
            index_of_replace_num = i - 1
            break
        i -= 1

    if index_of_replace_num == -1:
        return -1
    else:
        firstlist = numlist[:index_of_replace_num]
        replaced_num = numlist[index_of_replace_num]
        secondlist = numlist[index_of_replace_num+1:]
        new_replaced_num = 9
        i = 0
        delindex = 0
        while i < len(secondlist):
            if secondlist[i] > replaced_num and secondlist[i] < new_replaced_num:
                new_replaced_num = secondlist[i]
                delindex = i
            i += 1

        secondlist.pop(delindex)
        secondlist.append(replaced_num)
        firstlist.append(new_replaced_num)
        output = firstlist + sorted(secondlist)
        return int(''.join(str(x) for x in output))
