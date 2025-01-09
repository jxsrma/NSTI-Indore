class User:
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f'Username is:  {self.firstName} {self.lastName}'

    def __add__(self, obj: object):
        return f'{self.firstName} {self.lastName} has a friend name {obj.firstName} {obj.lastName}'

    def __del__(self):
        print(self.firstName, 'Object is Deleted')


astha = User('Astha', 'Prajapati')
damini = User('Damini', 'Batham')
neha = User('Neha', 'Yadav')

print(astha)
print(damini)

print(astha + damini)
print(damini + astha)

# del astha
# del damini

# print('******************')

# print(astha)
# print(damini)
