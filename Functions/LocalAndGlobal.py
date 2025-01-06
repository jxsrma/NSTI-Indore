x = 40


def localCheck():
    global x
    b = x + 30
    x = x+1
    # x += 12
    return x


print(x)
print(localCheck())
