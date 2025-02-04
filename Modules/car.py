import csv
import random
from datetime import datetime
import Tools

amount = 500000


# print("Your Car Intrest will be: ", Tools.si(amount, 8, 5))

# print(Tools.speed(200, 3))
# print(Tools.distance(80, 6))


# print(datetime.now())
# print(datetime.today().second)
# print(datetime.today().isoweekday())


marks = [
    ["roll", "Name", "Marks"],
    [1, "ABC", 55],
    [2, "DEF", 54],
    [3, "GHI", 52]
]

with open("Modules\\marks.csv", 'w') as file:
    write = csv.writer(file)
    for row in marks:
        write.writerow(row)

print('Successfully Created')
