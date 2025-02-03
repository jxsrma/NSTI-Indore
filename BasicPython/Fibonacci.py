start = 10
ending = 40

a = 0
b = 1
nums = []

while a <= ending:
    if a >= start:
        nums.append(a)
    c = a + b
    a = b
    b = c

print(nums)
