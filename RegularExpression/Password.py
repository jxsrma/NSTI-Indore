import re
passwordPattern = r'^[A-Za-z0-9@!\?#\$%\(\)\+&_-]{8,15}$'
strn = 'qwerto1@#?%$-()'
match = re.match(passwordPattern, strn)
if match:
    print('Pattern Matched: ', match.group())
else:
    print('Not Matched')
