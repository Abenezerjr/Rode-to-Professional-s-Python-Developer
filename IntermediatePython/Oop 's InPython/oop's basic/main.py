# item1='Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sumItem(self):
        return self.price * self.quantity


item1 = Item('Phone', 100, 5)
print(item1.name)

item2 = Item('Laptop', 1000, 3)
print(item2)
