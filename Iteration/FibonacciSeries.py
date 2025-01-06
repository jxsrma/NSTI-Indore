n1 = int(input("Enter Starting Number: "))
n2 = int(input("Enter Ending Number: "))

a, b = 0, 1

while b <= n2:
    if b >= n1:
        print(b, end=" ")
    a, b = b, a+b
