from datetime import datetime


class person:

    species = "Homo Sapiens"

    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def find_age(self):
        return datetime.now().year - int(self.dob.split('/')[2])

    def greet(self):
        print("Hello", self.species)

    @classmethod
    def get_data(cls):
        print(cls.species)

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __del__(self):
        print("deleted")


jash = person("Jash", "India", "03/08/2001")

print(jash.find_age())

print(person.is_adult(18))
person.get_data()

jash.greet()
del jash