count = 10

for i in range(1, count):
    for space in (count, 1, -1):
        print(space, end=" ")
    for j in range(1, i+1):
        print(f"({i},{j})", end=" ")
    print()
