def solution(s):
    out = []
    arr = []
    n = 2 
    for i in range(0, len(s), n):
        out.append(s[i:i+n])
    for i in out:
        if len(i) < 2:
            b = i
            b = b +"_"
            arr.append(b)
        else:
            arr.append(i)
    return arr
