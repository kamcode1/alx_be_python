class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero!"     
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero!"


        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    
item1 = Item("phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("keyboard", 75, 5)

print(Item.all)

# print(item2.price)
# item2.has_numpad = False
