import itertools
def permutations(string): return {''.join(i) for i in (itertools.permutations(string))}
