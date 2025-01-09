# from abc import ABC, abstractmethod


# class Person(ABC):
#     @abstractmethod
#     def print(self):
#         pass


# per1 = Person()

# print(per1)


# class Sum_Calculator():
#     def sumAllNumber(*args):
#         return sum(args)


# print(Sum_Calculator.sumAllNumber(5, 5, 10, 30))
import re
text = "+91-831-982-8866"
pattern = r"(\+91)?[-]?[0-9]{3}-[0-9]{3}-[0-9]{4}"


print(bool(re.match(pattern, text)))

email = "js_23@gmail.com"
pattern = r"[A-Za-z0-9_.]+@[A-Za-z]+\.[A-Za-z]{2,}"
print(bool(re.match(pattern, email)))
