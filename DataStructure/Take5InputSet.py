n = int(input("Enter Lenght for Set: "))

flag = True
setMain = set()
while flag:
    num = int(input("Enter Unique Number: "))
    if num in setMain:
        print("Already Present")
    else:
        setMain.add(num)
    if len(setMain) == n:
        flag = False
print(setMain)
