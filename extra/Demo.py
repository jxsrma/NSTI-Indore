class Student:

    def __init__(self, id: int, name: str):
        self.st_id = id
        self.name = name
        print("Student Object is Created")

    def print_details(self):
        print(f"{self.st_id}: {self.name}")


jash = Student(name="jash", id=23)
jash.print_details()
