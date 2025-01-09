import json
# student = {
#     'name': 'Shyam',
#     'class': '10',
#     'section': 'B',
#     'school': 'XYZ'
# }

# with open('school_data.json', 'w') as jsonFile:
#     json.dump(student, jsonFile)

# student['marks'] = 67

# with open('school_data.json', 'w') as jsonFile:
#     json.dump(student, jsonFile)

with open('school_data.json', 'r') as jsonFile:
    studentdata = json.load(jsonFile)
    student = studentdata

student['marks'] = student['marks']+1

with open('school_data.json', 'w') as jsonFile:
    json.dump(student, jsonFile)
