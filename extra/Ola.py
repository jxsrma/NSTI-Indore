class Person:
    def __init__(self, name, contact_info):
        self.name = name
        self.__contact_info = contact_info

    def get_contact_info(self):
        print("ContactInfo: ", self.__contact_info)


class Driver(Person):
    def __init__(self, name, contact_info, driver_rating: int, license_number):
        super().__init__(name, contact_info)
        self.driver_rating = driver_rating
        self.license_number = license_number

    def login(self):
        print("driver login")

    def accept_ride(self, rider):
        print("ride accepted: ", rider.name)
        rider._ride_accepted(self)


class Rider(Person):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)

    def login(self):
        print("driver login")

    def _ride_accepted(self, driver):
        print("ride accepted by: ", driver.name)

from abc import ABC, abstractmethod
class Ride():
    def calculate_price():
        pass

rider1 = Rider("Jash", "1234123412")
driver1 = Driver("Ram", "1234123412", 4.5, "1234567890")

driver1.accept_ride(rider1)