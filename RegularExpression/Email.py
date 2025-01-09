# ab.Cd_12-4@gmail.com
import re

EmailPattern = r'^[A-Za-z0-9\+._-]+@[a-z]+\.[a-z]{2,}(\.[a-z]{2,})?$'

# strn = 'abAdnjAsasdjn654c.+-123812938718@gmailyahoo.company'
# strn = input('Enter Email for Verification:: ')
# match = re.match(EmailPattern, strn)
# if match:
#     print('Pattern Matched: ', match.group())
# else:
#     print('Not Matched')

passwordPattern = r'^[A-Za-z0-9@!\?#\$%-\(\)\+&_]{8,15}$'
strn = '#12fiawhfiwmhfcoiwer239842348i2nfi2i3r'
match = re.match(passwordPattern, strn)
if match:
    print('Pattern Matched: ', match.group())
else:
    print('Not Matched')
