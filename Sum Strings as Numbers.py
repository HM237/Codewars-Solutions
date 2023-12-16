def sumdigits(c, a=0, b=0):
        s = a + b + c
        if s >= 10:
            c = s // 10
            s = s % 10
        else:
            c = 0
        return s, c
def sum_strings(x, y):
        i = len(x)
        j = len(y)
        c = 0
        out = []
        while i > 0 and j > 0:
            s, c = sumdigits(c, int(x[i-1]), int(y[j-1]))
            out.append(s)
            i -= 1
            j -= 1
        while i > 0:
            s, c = sumdigits(c, int(x[i-1]))
            out.append(s)
            i -= 1
        while j > 0:
            s, c = sumdigits(c, int(y[j-1]))
            out.append(s)
            j -= 1
        if c > 0:
            out.append(c)
        out = ''.join([str(n) for n in reversed(out)]).lstrip("0")
        if out:
            return out        
        return "0"
