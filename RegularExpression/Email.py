# ab.Cd_12-4@gmail.com
import re

EmailPattern = r'^[A-Za-z0-9\+\._\-]+@[a-z]+\.[a-z]{2,}(\.[a-z]{2,})?$'
EmailPattern = r'^[A-Za-z0-9\+\._\-]+@gov.in$'

strn = 'abAdnjAsasdjn654c.+-123812938718@gmailyahoo.company'
# strn = input('Enter Email for Verification:: ')
match = re.match(EmailPattern, strn)
if match:
    print('Valid Email: ', match.group())
else:
    print('invalid Email')
