n = 3


def func():
    print("Hello")
    global n
    n += 1
    return n


print(func())

print(n)