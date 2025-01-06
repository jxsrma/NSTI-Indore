# with open("FileHandling\HNY.txt") as file:
#     content = file.read()
#     print(content)


# print("********Above was the file content*********")
# print(content)

with open("FileHandling/HNY.txt", 'ba') as file:
    # content = file.read()
    # print(content)
    # print(type(content))

    file.write(b'\nData')
