def stringpal(s):
    n = len(s)
    for r in range(n):
        if s[r] != s[n - r - 1]:
            return False
    return True