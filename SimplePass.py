def passcheck(pas):
    realpas = "password"
    typing = input("Enter your password")
    while realpas != typing:
        typing = input("Incorrect password, try again")
    print("Correct password, logging you in")