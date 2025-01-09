import re

# string = "Hello World! Welcome to Python regex."
# pattern = r"Hello"

# match = re.match(pattern, string)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match found.")

# string = "Learning Python regex is fun!"
# pattern = r"Python"

# search = re.search(pattern, string)
# if search:
#     print(search.group())
# else:
#     print("Not found")

# string = "cat bat mat rat cat bat"
# pattern = r"cat|bat"

# match = re.findall(pattern,string)
# print(match[3])

# string = "123-456-789, 987-654-321, 456-789-123"
# pattern = r"\d{3}-\d{3}-\d{3}"

# matches = re.finditer(pattern, string)

# for match in matches:
#     print(match.group(), " : ", match.start())

# string = "Phone: 123-456-789, ID: 987654321"
# pattern = r"\d"

# result = re.sub(pattern, "Num", string)
# print("Replaced String:", result)

# string = "apple,,,, banana orange, grape"
# pattern = r"[,\s]+"

# result = re.split(pattern, string)
# print(result)

# pattern = r"a.c"
# string = "abc, adc, aec, axc"

# match = re.findall(pattern, string)
# print(match)

# pattern = r"^Hello"
# string = "Hello World! Hello Again!"

# match = re.search(pattern, string)
# print(match.group())

# pattern = r"Python$"
# string = "I love Python"
# match = re.search(pattern, string)
# print(match.group())

# pattern = r"ba*"
# string = "b, ba, baa, baaa"
# matchs = re.findall(pattern, string)
# print(matchs)

# pattern = r"ba+"
# string = "b, ba, baa, baaa"
# matchs = re.findall(pattern, string)
# print(matchs)

# pattern = r"ba?"
# string = "b, ba, baa, baaa"
# matchs = re.findall(pattern, string)
# print(matchs)

# pattern = r"a{2}"
# string = "a aa aaa aaaa"
# matchs = re.findall(pattern, string)
# print(matchs)

# pattern = r"a{2,}"
# string = "a aa aaa aaaa"
# matchs = re.findall(pattern, string)
# print(matchs)

# pattern = r"a{2,3}"
# string = "a aa aaa aaaa"
# matchs = re.findall(pattern, string)
# print(matchs)

# pattern = r"[aeiou]"
# string = "hello world"
# matchs = re.findall(pattern, string)
# print(matchs)

# pattern = r"cat|dog"
# string = "I have a cat and a dog."
# matches = re.findall(pattern, string)
# print(matches)


# str1 = """
# The quick brown fox jumps over the lazy dog.
# Foxes are wild animals. The dog quickly ran away.
# My email is example@example.com and my number is (123) 456-7890
# """
# pattern = r"(\bil\b)"
# match = re.findall(pattern, str1)
# print(match)

# def vEmail(email):
#     pattern = r"^[\w\d._]+@[\w]+\.[\w]{2,}$"
#     return bool(re.match(pattern,email))

# print(vEmail("jashsharmag@mail.mm"))

# def contact_check(contact):
#     pattern = r"^(\+91)-[\d]{3}-[\d]{3}-[\d]{4}"
#     return bool(re.match(pattern, contact))

# print(contact_check("+91-831-982-8866"))
