def largest(n, xs):
    xs = sorted(xs, reverse=True)
    return sorted(xs[:n])
