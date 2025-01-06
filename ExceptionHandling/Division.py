try:
    a = int(input("Please enter number 1: "))
    b = int(input("Please enter number 2: "))
    c = a/b
except ZeroDivisionError as zde:
    print("Please do Not divide it by zero")
    c = a/1
else:
    print("this is else")
finally:
    print("this is finally")
print(c)
print("This is a program")

# li = [1, 2, 3, 4]

# try:
#     prin("hello")
# except NameError as ne:
#     print("Please User, correct the Name, Else dont try to program: ", ne)
# except IndentationError as ie:
#     print("Please correct the Indentation: ", ie)
# except Exception as e:
#     print("Unknown Error: ", e)


# print("programm is successfully Executed")
