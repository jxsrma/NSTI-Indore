def student(**kwargs):
    print("This is student information")
    for key, value in kwargs.items():
        print(key, " :\t", value)


student(firstName="Damini", lastName="Batham",
        roll=35, maths=17, accounts=15, city="Indore")
print()
