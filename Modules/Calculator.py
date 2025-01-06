pi = 22/7


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mult(a, b):
    return a*b


def div(a, b):
    return a/b


def mod(a, b):
    return a % b


def printMultipleTimesMyName(name: str, num: int):
    """This Function will print Name mutiple times"""
    for i in range(num+1):
        print("Hello", name)


if __name__ == "__main__":
    print("this is a module for basic calculation")
