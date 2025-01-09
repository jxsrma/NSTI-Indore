# Method Overriding
# class Animal:
#     def speak():
#         print('Animal can speak')


# class Dog(Animal):
#     def speak():
#         print('Bark')


# class Cat(Animal):
#     def speak():
#         print('Meow')


# Animal.speak()
# Dog.speak()
# Cat.speak()


# Duck Typing
class Animal:
    def walk(self):
        print("animal is walking")

    def speak(self):
        print('Animal can speak')


class Dog:
    def guard(self):
        print('Dog is Guarding the Door')

    def speak(self):
        print('Bark')


class Cat:
    def climb(self):
        print('Cat is Climbing the tree')

    def speak(self):
        print('Meow')


class Car:
    def drive(self):
        print('Car is driving by someone')

    def Horn(self):
        print('Horn is applied')


class Truck:
    def drive(self):
        print('Truck is driving by someone')

    def Horn(self):
        print('Horn is applied')


def MakeAnimalSpeak(obj: object):
    obj.speak()


def MakeVehicalDrive(obj: object):
    obj.drive()
    obj.Horn()


ani = Animal()
dog = Dog()
cat = Cat()
car = Car()
tru = Truck()

# MakeAnimalSpeak(ani)
# MakeAnimalSpeak(dog)
# MakeAnimalSpeak(cat)
# MakeAnimalSpeak(car)

MakeVehicalDrive(car)
MakeVehicalDrive(tru)
MakeVehicalDrive(ani)
MakeVehicalDrive(dog)
MakeVehicalDrive(cat)
