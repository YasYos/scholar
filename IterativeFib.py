first = 0
second = 1
nx = 0
n = 5
for r in range(n):
    nx = first + second
    first = second
    second = nx
print(nx)
