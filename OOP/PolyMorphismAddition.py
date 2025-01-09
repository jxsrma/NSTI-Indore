class Addition:
    def add(a, b, c=0, d=0, e=0):
        return a+b+c+d+e


class Multiply:
    def add(a, b, c=1, d=1, e=1):
        return a*b*c*d*e


print(Addition.add(5, 5))
print(Addition.add(5, 5, 5))
print(Addition.add(5, 5, 5, 5))
print(Addition.add(5, 5, 5, 5, 5))
print(Multiply.add(5, 5))
print(Multiply.add(5, 5, 5))
print(Multiply.add(5, 5, 5, 5))
print(Multiply.add(5, 5, 5, 5, 5))
