def minmax(ls):
    """
    Returns tuple (min, max)
    """
    m = n = ls[0]
    for r in ls:
        if m > r:
            m = r
        if n < r:
            n = r
    return (m, n)