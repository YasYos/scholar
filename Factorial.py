def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fact(n):
    p = 1
    for r in range(1, n + 1):
        p *= r
    return p
