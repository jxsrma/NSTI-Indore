pi = 3.14
g = 9.8

# ((9/5)*c)+32
def CtoF(c):
    f = ((9/5)*c)+32
    return f

# (F-32)*(5/9)


def FtoC(f):
    c = (f-32)*(5/9)
    return c

# d = s*t


def distance(s: int, t: int):
    d = s*t
    return d

# s = d/t


def speed(d: int, t: int):
    s = d/t
    return s

# t = d/s


def time(d: int, s: int):
    t = d/s
    return t


# a = (b**2 + c**2)**0.5
def pgt(b: float, c: float):  # Pythagorus Theorem
    a = (b**2 + c**2)**0.5
    return a

# si = (p*r*t)/100


def si(p: int, r: int, t: int):  # Simple Instrest
    si = (p*r*t)/100
    return si
