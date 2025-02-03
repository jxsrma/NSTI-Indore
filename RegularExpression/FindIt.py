import re

strn = 'Hello AI, Today is Wednesday 8TH January 2025. We ARE learning Regular Expression in the AIPA Lab room number 112. hello your OTP is 666789, ISRO, NASA, AS'

patt = r'[A-Z]{2,}'

# match = re.findall(patt, strn)
# if match:
#     print(match)
# else:
#     print('Not Found')

count = 1
print("List of Abb in the Given Paragraph:")
for abbrevation in re.finditer(patt, strn):
    print(count, abbrevation.group())
    count += 1

# patt1 = r'[Hello]*[We]*'
# replace = re.sub(patt1, 'Happy', strn)

# print(replace)
