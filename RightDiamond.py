def rightdiamond(h):
    f = h//2
    for r in range(f):
        for s in range(r):
            print('* ', end='')
        print()
        
    for r in range(f):
        for s in range(f - r):
            print('* ', end='')
        print()