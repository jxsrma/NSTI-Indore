# def create():
#     with open("Students.txt", "w") as file:
#         file.write("ID: 101, Name: Alice, Age: 20\n")
#         file.write("ID: 102, Name: Bob, Age: 21\n")
#         file.write("ID: 103, Name: Charlie, Age: 19\n")


# def display():
#     with open("Students.txt", "r") as file:
#         for line in file:
#             print(line)


# def search(id):
#     with open("Students.txt", "r") as file:
#         for line in file:
#             if f"ID: {id}" in line:
#                 print(line.strip())
#                 print("Student Found")
#         return
#     print("Student not Found")


# def add(id: int, name, age):
#     with open("Students.txt", "a") as file:
#         file.write(f"ID: {id}, Name: {name}, Age: {age}\n")


# add("23", "J", 23)
# display()


def create():
    file = open("Students1.txt", "w")
    file.write("ID: 101, Name: Alice, Age: 20\n")
    file.write("ID: 102, Name: Bob, Age: 21\n")
    file.write("ID: 103, Name: Charlie, Age: 19\n")
    file.close()


def display():
    file = open("Students1.txt", "r")
    for line in file:
        print(line.strip())
    file.close()


def search(id):
    file = open("Students1.txt", "r")
    for line in file:
        if f"ID: {id}" in line:
            print(line.strip())
            print("Student Found")
            return
    print("Student not Found")


# def add(id: int, name, age):
#     with open("Students.txt", "a") as file:
#         file.write(f"ID: {id}, Name: {name}, Age: {age}\n")

# create()
# display()
search(103)

# add("23", "J", 23)
