def sumavg(n):
    """
    Returns a tuple of the sum and average
    """
    s = 0
    i = float(input("Enter a number"))
    while i != 0:
        s += i
        i = float(input("Enter another number"))
        
    return (s, s/n)