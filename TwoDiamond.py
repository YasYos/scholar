n = 5
for r in range(n):
    for s in range(n - r):
        print(' ', end='')
    for t in range(2*r-1):
        print('*', end='')
    print()
for r in range(n):
    for s in range(r):
        print(' ',end='')
    for t in range(2*(n-r) -1):
        print('*', end='')
    print()
