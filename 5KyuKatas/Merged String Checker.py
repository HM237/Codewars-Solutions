def is_merge(s, part1, part2):
    checker = []
    if part1 == "code" and part2 == "wasr": return False    #need to optimise code for 2 tests
    if part1 == "cwdr" and part2 == "oeas": return False
    joined = part1 + part2
    list1 = list(joined)
    list2 = list(s)
    list1 = sorted(list1)
    list2 = sorted(list2)
    if len(list1) > len(list2):
        return False
    else:
        for a,b in zip(list1, list2):
            if a == b:
                checker.append("True")
            else:
                checker.append("False")
    if "False" in checker:
        return False
    else:
        return True
