li = [2, 6, 7, 5, 3]
sum = 13

for i in li:
    if (sum - i) in li:
        print(sum-i, i)
        break
