import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero!"     
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero!"


        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    #property
    def price(self):
        return self.__price
    
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            #print(item)
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
   
    @staticmethod
    def is_integer(num):
        # We will coun out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
