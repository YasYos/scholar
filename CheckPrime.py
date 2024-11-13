def prime(n):
    for r in range(2, n//2 + 1):
        if n % r == 0:
            return False
    return True