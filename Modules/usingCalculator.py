import Calculator as c
from datetime import datetime

a = 10
b = 20

print(c.pi)
print(c.add(a, b))
print(c.sub(a, b))
print(c.mult(a, b))
print(c.div(a, b))
print(c.mod(a, b))

p = 20000
r = 12
t = 2

#(p*r*t)/100

print(c.div(
    c.mult(
        c.mult(p,r),t
        )
    ,100)
      )

c.printMultipleTimesMyName(datetime.now(),20000)