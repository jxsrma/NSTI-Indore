from abc import ABC, abstractmethod

# Abstract Class


class Area(ABC):

    # Abstract Method
    @abstractmethod
    def areaCircle(self):
        pass

    @abstractmethod
    def areaRectangle(self):
        pass


class calculateArea(Area):

    def areaCircle(self, r):
        return (22/7)*r**2
    
    def areaRectangle(self, l, b):
        return l*b


c = calculateArea()


print(c.areaCircle(5))
print(c.areaRectangle(5, 2))
