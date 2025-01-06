class State:

    Country = "India"

    def __init__(self, name, capital, population, landmark, food):
        self.name = name
        self.capital = capital
        self.population = population
        self.landmark = landmark
        self.food = food

        print("State Object is created")

    def printDetails(self):
        print("Name: ", self.name)
        print("Capital: ", self.capital)
        print("Population: ", self.population)
        print("Landmark: ", self.landmark)
        print("Food: ", self.food)


class Person:

    def __init__(self, name, age, address="Indore"):
        self.name = name
        self.age = age
        self.address = address

    def printDetails(self):
        print("Name: ", self.name)
        print("age: ", self.age)
        print("Address: ", self.address)
