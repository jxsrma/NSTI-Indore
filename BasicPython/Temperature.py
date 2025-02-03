temp = input()

# 45f

degree = int(temp[:-1])
type_ForC = temp[-1]

print(degree)
print(type_ForC)


if type_ForC == 'c' or type_ForC == 'C':
    c = degree
    result = (9/5)*c + 32
    print(result)

elif type_ForC == 'f' or type_ForC == 'F':
    f = degree
    result = (5/9)*(f - 32)
    print(result)

else:
    print('Invalid')
