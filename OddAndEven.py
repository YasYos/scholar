def oddandeven(ls):
    """
    Returns odd and even tuple
    """
    ev = od = 0
    for r in ls:
        if r % 2 == 0:
            ev += 1
        else:
            od += 1
    return (od, ev)