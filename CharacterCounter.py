def charcounter(s):
    s = "exampleeee"
    howmany = {}

    for c in s:
        if c not in howmany:
            howmany[c] = 1
        else:
            howmany[c] += 1
    return howmany