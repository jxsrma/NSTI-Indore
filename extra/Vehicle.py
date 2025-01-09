import datetime


class Vehicle:
    brand: str
    model: str

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)

    def _calculate_age(self, dom):
        print("Age of Vehicle", datetime.date.today().year - dom)

    def __internal_check(self):
        print("Internal Check Completed")


class Car(Vehicle):
    fuel_type: str

    def __init__(self, brand, model, fuelType):
        super().__init__(brand, model)
        self.fuel_type = fuelType

    def display_info(self):
        super().display_info()
        print("Fuel Type: ", self.fuel_type)
        super().display_info()


class ElectricCar(Car):
    battery_capacity: int

    def __init__(self, brand, model, fuelType, battery_capacity):
        super().__init__(brand, model, fuelType)
        self.battery_capacity = battery_capacity

    def display_range(self):
        print("Range: ", self.battery_capacity * 5)


class HeavyLoad():
    load_capacity: int

    def __init__(self, load_capacity):
        self.load_capacity = load_capacity

    def check_overload(self, load):
        if load > self.load_capacity:
            print("Over Loaded!!")
        else:
            print("Safe Load")


class Truck(Vehicle, HeavyLoad):
    def __init__(self, brand, model, load_capacity):
        Vehicle.__init__(self, brand, model)
        HeavyLoad.__init__(self, load_capacity)

    def display_info(self, load):
        Vehicle.display_info(self)
        HeavyLoad.check_overload(self, load)


if __name__ == "__main__":
    tata = Truck("Tata", "Truck", 50)
    tata.display_info(50)
