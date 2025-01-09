from abc import ABC, abstractmethod


class User(ABC):

    name: str
    email: str

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def view_account_details():
        pass

    @abstractmethod
    def place_order():
        pass


class Customer(User):

    order_history: list

    def __init__(self, name, email):
        super().__init__(self, name, email)

    def place_order(order_details):
        print(order_details)

    def view_account_details(self):
        print(self.name, self.email)

    def view_order_history(self):
        print(self.order_history)


class Admin(User):
    admin_id: str

    def __init__(self, name, email, admin_id):
        super().__init__(name, email)
        self.admin_id = admin_id

    def place_order(order_details):
        print(order_details)

    def view_account_details(self):
        print(self.name, self.email)

    def add_product(product):
        print("added")

    def remove_product(product_id):
        print("removed")

    def view_all_orders():
        print("All orders")

class Product:
    product_id:str
    name:str
    price:float
    stock:int
    
    def update_stock(new_stock):
        print("updated")
    def get_details():
        print("details")