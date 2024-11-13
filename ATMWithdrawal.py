account = 1000000
print(f'You have ${account} in your account')
dep = float(input('Enter how much you\'d like to withdraw\n'))
while dep > account:
    dep = float(input('Enter how much you\'d like to withdraw\n'))
account -= dep
print(f'Your account is now {account}')
