import re

strn = 'Hello, Today is Wednesday 8th January 2025. We are learning Regular Expression in the AIPA Lab room number 112.'

# patt = r'[A-Z][a-z]{4}'

# match = re.findall(patt, strn)
# if match:
#     print(match)
# else:
#     print('Not Found')


patt1 = r'[Hello]*[We]*'
replace = re.sub(patt1, 'Happy', strn)

print(replace)
