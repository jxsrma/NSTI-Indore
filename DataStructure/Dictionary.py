student = {
    'name': 'Megha',
    'class': 'AI Trade',
    'city': 'Indore',
    'rollNo': '14',
}
# print(student['name'])
# print(student['class'])
# print(student['city'])
# print(student['rollNo'])

student['marks'] = 33.33
student['dob'] = 2006
student['attendance'] = True
student['subjects'] = ['Maths', 'Physics', 'Hindi']
student['sister'] = {
    'name': 'Alka',
    'class': 'AI Trade',
    'city': 'Indore',
    'rollNo': '15',
    'dob': 2006,
    'attendance':  True,
    'subjects': ['Maths', 'Physics', 'Hindi']
}

# print(student.pop('subjects'))
# print(student.get("city1","This key is not present in the dict"))

# tableOfTwo = {x: x for x in range(1, 6) if x > 2}
# print(tableOfTwo)

for key, value in student.items():
    print(key, '   ::    ', value)
