
class Product:
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

    @property
    def get_name(self):
        return self.name

    @name.setter
    def set_name(self, new_name):
        self.name = new_name
    
    @property
    def get_price(self):
        return self.price

    @price.setter
    def set_price(self, new_price):
        self.price = new_price

    @property
    def get_description(self):
        return self.description

    @description.setter
    def set_description(self, new_description):
        self.description = new_description
