"""
Alphabets
Digits
Special Character
minimum 8 keywords
"""
import re

password = "J@sh1_?2348_!88"

alphabet = False
digits = False
symbols = False
space_not_included = True

if len(password) > 8:

    for i in password:

        if alphabet or re.match(r"\w", i):
            alphabet = True

        if digits or re.match(r"\d", i):
            digits = True

        if symbols or re.match(r"[?+!.@#$%^&*_]", i):
            symbols = True
        if re.match(r"[\s]", i):
            space_not_included = False
    if alphabet and digits and symbols and space_not_included:
        print("strong password")
    else:
        print("Not Strong", alphabet, digits,
              symbols, space_not_included)
else:
    print("smaller than 8")
