def multi(*args):
    """This function will sum all the given values"""

    multi = 1
    for num in args:
        multi *= num

    return multi


result = multi(5,3,55,70,60)
print(result)
