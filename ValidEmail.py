import re

def valemail(e):
    return re.match(r"^.+@.+\.", e) is not None