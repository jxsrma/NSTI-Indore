from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop():
        pass


class Suzuki(Car):
    def start(self):
        print("Car Started")

    def stop(self):
        print('Car stop')

swift = Suzuki()
swift.start()
swift.stop()
