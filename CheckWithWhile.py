def checkinp(inp):
    """
    This checks if the input is in [0, 100]
	In general, the while can have any condition.
    """
    while inp < 0 or inp > 100:
        inp = int(input("Pick a number that\'s between 0 and 100."))
    print("Valid input")