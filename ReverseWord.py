def reverseword(word):
    rev = ''
    n = len(word)
    for c in range(n):
        rev += word[n - c - 1]
    return rev