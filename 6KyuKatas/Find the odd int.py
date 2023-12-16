def find_it(seq):
    for x in seq:
        a = seq.count(x)
        if a % 2 != 0:
            return x
