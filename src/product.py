class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация класса с атрибутами продукта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params_product: dict):
        cls.name = params_product["name"]
        cls.description = params_product["description"]
        cls.price = params_product["price"]
        cls.quantity = params_product["quantity"]
        return cls

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, prices):
        if prices <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = prices
