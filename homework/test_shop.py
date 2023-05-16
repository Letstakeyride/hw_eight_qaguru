import pytest
from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999) is True, 'Количество больше запрашиваемого'
        assert product.check_quantity(1000) is True, 'Количество равно запрашиваемуму'
        assert product.check_quantity(1001) is False, 'Количество меньше запрашиваемого'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(0)
        assert product.quantity == 1000, 'Некорректный остаток после покупки 0 шт'
        product.buy(100)
        assert product.quantity == 900, 'Некорректный остаток после покупки 100шт'
        product.buy(900)
        assert product.quantity == 0, 'Некорректный остаток после покупки 900шт'

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001), 'ValueError'


class TestCart:

    def test_product_add(self, cart, product):
        assert len(cart.products) == 0, 'Проверка на пустую корзину'
        cart.add_product(product)
        assert cart.products[product] == 1, 'Проверка на добавление'
        cart.add_product(product, 100)
        assert cart.products[product] == 101, 'Проверка на дополнение'
        assert len(cart.products) == 1, 'Проверка на типы '

    def test_product_remove(self, cart, product):
        cart.add_product(product, 500)
        cart.remove_product(product, 400)
        assert cart.products[product] == 100, 'Проверка на удаление нужного количества'
        cart.remove_product(product)
        assert len(cart.products) == 0, 'Удаление без указания количества'
        cart.add_product(product, 500)
        cart.remove_product(product, 550)
        assert len(cart.products) == 0, 'Проверка условия на удаление больше чем есть'
        cart.add_product(product, 500)
        cart.remove_product(product, 500)
        assert len(cart.products) == 0, 'Удаление польностью с указанием количества'

    def test_product_clear(self, cart, product):
        cart.add_product(product, 500)
        cart.clear()
        assert len(cart.products) == 0, 'Очистка'

    def test_product_get_total_price(self, cart, product):
        cart.add_product(product, 100)
        assert cart.get_total_price() == 10000, 'Проверка подсчёта итоговой стоимости'

    def test_product_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert len(cart.products) == 0, 'Проверка покупки'
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy(), "Провера Value error"
