def commelems(ls1, ls2):
    se1 = set()
    se2 = set()
    for r in ls1:
        se1.add(r)
    for r in ls2:
        if r in se1:
            se2.add(r)
    return se2