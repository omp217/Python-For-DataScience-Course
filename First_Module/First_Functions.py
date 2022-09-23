# %%
def checkifnotnumeric(**args):
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True

# %%
def addall(*args):
    """ This is documentation of this function"""
    sum = 0
    for x in args:
        sum += x
    return sum

# %%
myname = "Python"


