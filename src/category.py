class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация класса с атрибутами категории товара"""
        self.name = name
        self.description = description
        self.__products = products
        self.category_count += 1
        self.product_count += len(products)

    def add_product(self, new_products):
        self.__products.append(new_products)
        self.product_count += 1

    @property
    def products(self):
        for product in self.__products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return
