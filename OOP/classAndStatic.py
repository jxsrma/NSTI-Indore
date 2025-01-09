class Person:
    country = "India"
    institute = 'Indore'

    def __init__(self, name):
        self.name = name
        print('Constructor created Person Object')

    @classmethod
    def printDetails(cls):
        print('Country: ', cls.country)
        print('institute: ', cls.institute)

    @staticmethod
    def age(by, cy):
        print(cy-by)
        print('this is static Method')
    
    @classmethod
    def age(cls,by, cy):
        print(cy-by)
        print('this is class Method')


# user = Person('Shyam')
# print(user.name)

# Person.printDetails()
Person.age(2003, 2024)
# print(Person.country)
