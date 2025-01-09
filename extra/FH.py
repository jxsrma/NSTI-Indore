import csv

def create():
    with open("marks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Maths", "Science", "English"])
        writer.writerow([101, "Alice", 78, 85, 92])
        writer.writerow([102, "Bob", 88, 76, 81])
        writer.writerow([103, "Charlie", 90, 80, 85])

def read():
    with open("marks.csv", "r") as file:
        reader = csv.reader(file)
        # print(type(reader))
        for row in reader:
            print(row)
read()