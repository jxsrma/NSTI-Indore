# +91-123-456-7890

import re

mobilePattern = r'^(\+91)?-?[\d]{3}-[\d]{3}-[\d]{4}$'

strn = '+91-123-544-4533'
match = re.match(mobilePattern, strn)
if match:
    print(match.group())
else:
    print('Not Matched')
