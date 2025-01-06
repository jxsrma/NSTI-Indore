import csv
# data = [
#     ['id', 'roll', 'name', 'age'],
#     [1, 'AI101', 'Ishan', 15],
#     [2, 'AI102', 'Astha', 16],
#     [3, 'AI103', 'Vijayshree', 17],
#     [3, 'AI103', 'Vijayshree', 17],
#     [3, 'AI103', 'Vijayshree', 17],
#     [3, 'AI103', 'Vijayshree', 17],
#     [3, 'AI103', 'Vijayshree', 17],
#     [3, 'AI103', 'Vijayshree', 17],
#     [3, 'AI103', 'Vijayshree', 17],
# ]

# with open('FileHandling\students.csv', 'w', newline='') as CSVfile:
#     writer = csv.writer(CSVfile)
#     writer.writerows(data)

# studentData = []

# with open('FileHandling/students.csv', 'r') as CSVfile:
#     reader = csv.reader(CSVfile)

#     studentData = list(reader)

#     # for row in reader:
#     #     studentData.append(row)

# print(studentData)
# for row in studentData:
#     print(row)

file = open('C:\\Users\\Jash\\Desktop\\student.csv', 'r')
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()
