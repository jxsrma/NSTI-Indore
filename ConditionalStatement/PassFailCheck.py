marks = int(input("Enter student's marks: "))

if marks < 0 or marks >= 100:
    print("Please enter correct marks")
elif marks >= 75:
    print("Pass")
else:
    print("Fail")