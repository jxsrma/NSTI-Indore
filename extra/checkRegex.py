import re
ptrn = r"^[\w\d._]+@[\w\d]+\.[\w]{2,}$"

str1 = "jashsharma@gmail.com"

match = bool(re.match(ptrn, str1))
print(match)


ptrn1 = r"\((\d){3}\)\s(\d){3}-(\d){4}"

str2 = "(123) 456-7890"


match1 = bool(re.match(ptrn1, str2))
print(match1)

ptrn2 = r"[\w\d@_#.!?$%]{8,}"
str3 = "J@s#1234"

match2 = bool(re.match(ptrn2, str3))
print(match2)