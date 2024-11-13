def firstletter():
    for r in range(5):
        for s in range(r):
            print(' ', end='')
        print('*',end='')
        for s in range(r, 9 - r):
            print(' ', end='')
        print('*')
    for r in range(5):
        for s in range(5):
            print(' ', end='')
        print("*")