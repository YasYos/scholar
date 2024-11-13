def twolistdict(ls1, ls2):
    d = dict()
    for r, s in zip(ls1, ls2):
        d[r] = s
    return d