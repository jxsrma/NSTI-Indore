class Animals:

    def __init__(self):
        print("This is Animal Class")

    def speak(self):
        print("This Animal Speak")


class Mammals(Animals):
    furr: bool

    def __init__(self, DoesHaveFurr):
        print("This is Mammal Class")
        self.furr = DoesHaveFurr
        super().speak()

        if self.furr:
            print("Have Furr")


class Dog(Mammals):
    def __init__(self,furr):
        print("This is a Dog Class")
        super().__init__(True)


mammal1 = Dog(False)
