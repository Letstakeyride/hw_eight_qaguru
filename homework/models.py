import dataclasses


@dataclasses.dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:

        if quantity <= self.quantity:
            return True
        else:
            return False

    def buy(self, quantity):

        if not self.check_quantity(quantity):
            raise ValueError('Недостаточное количество продукта')
        else:
            self.quantity -= quantity

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):

        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):

        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = sum(product.price * quantity for product, quantity in self.products.items())
        return total_price

    def buy(self):

        for product, quantity in self.products.items():
            if not product.check_quantity(quantity):
                raise ValueError(f"Недостаточное количество продуктов {product.name}")
            else:
                product.buy(quantity)
        self.clear()
