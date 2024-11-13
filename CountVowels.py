vowels={'a','e','i','o','u','A','E','I','O','U'}
vees = 0
S = 'stringexample'
for c in S:
    if c in vowels:
        vees += 1
print(vees)