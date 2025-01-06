count = 10

for i in range(1, count):
    for space in range(count-i, 1, -1):
        print(end=" ")
    for j in range(1, i+1):
        print(f"*", end=" ")
    print()
