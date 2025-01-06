def ASCbyString(num):
    strNum = str(num)
    sum = 0
    for i in strNum:
        sum += int(i)**3
    if sum == num:
        return True
    else:
        return False


def ASCbyMaths(num):
    backNum = num
    sum = 0
    while num > 0:
        sum += (num % 10)**3
        num = int(num/10)

    if sum == backNum:
        return True
    else:
        return False


num = 153
print(ASCbyMaths(num))
print(ASCbyMaths(370))
print(ASCbyMaths(789))

# print(ASCbyString(num))
# print(ASCbyString(345))
# print(ASCbyString(345))

aslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725,
          4210818, 9800817, 9926315, 24678050, 24678051, 88593477, 146511208, 472335975, 534494836, 912985153, 4679307774]

# for i in range(1, 999):
#     if ASCbyString(i):
#         print(i)
