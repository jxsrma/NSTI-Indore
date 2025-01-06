totalCount = 0
FinishLine = 100
ChildLocation = 0
while ChildLocation < 100:
    totalCount += 1
    ChildLocation += 3
    ChildLocation -= 1
    print(f"{ChildLocation}, {totalCount}")
print(totalCount)
