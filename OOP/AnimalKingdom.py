class Animal:
    def __init__(self, gender: str, breed: str, domesticated: bool):
        self.gender = gender
        self.breed = breed
        self.domesticated = domesticated

    def speak(self):
        print(self.name, "speaking")

    def Walking(self):
        print(self.name, "walking")


class tiger(Animal):
    def __init__(self, name, weight, color, gender, breed, domesticated):
        self.name = name
        self.weight = weight
        self.color = color
        super().__init__(gender, breed, domesticated)

    def roar(self):
        print("Tiger is Roaring")

    def sleeping(self):
        print("Tiger is sleeping")


# t = tiger('Sheru', 100, 'Brown', 'M', 'Bengal', False)
# t.roar()
# t.sleeping()
# t.Walking()
# t.speak()
# print(t.breed)
# print(t.gender)
# print(t.domesticated)

simba = tiger('Simba', 150, 'Orange', 'M', 'Asian', True)

simba.roar()
print(simba.name)
print(simba.color)