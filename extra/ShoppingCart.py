class ShoppingCart:
    content = dict()

    def add(self, name, price: int):
        self.content[name] = price

    def remove(self, name):
        self.content.pop(name)

    def calculate_total(self):
        total = 0
        for key, val in self.content.items():
            print(key, ":", val)
            total += int(val)
        print("Total : ", total)


dmart = ShoppingCart()

dmart.add("Chocolates", 10)
dmart.add("Bread", 50)

dmart.calculate_total()

dmart.remove
