def same_case(a, b):
    if (a.isalpha() == False) or (b.isalpha() == False): return -1
    elif ((a.lower() == a) and (b.lower() == b)) or ((a.upper() == a) and (b.upper() == b) ): return 1
    elif ((a.lower()== a) and (b.upper() == b)) or ((a.upper() == a) and (b.lower() == b)): return 0
