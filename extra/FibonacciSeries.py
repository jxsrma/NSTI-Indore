start = 10
end = 50

a, b = 0, 1

fs = []

while a <= end:
    if a >= start:
        fs.append(a)
    a, b = b, a+b

print(fs)
