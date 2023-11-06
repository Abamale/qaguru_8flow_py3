"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity - 1)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(product.quantity)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_cart_add_product(self, product, cart):
        cart.add_product(product)
        assert product in cart.products
        assert cart.products.get(product) == 1

    def test_cart_remove_product(self, product, cart):
        cart.add_product(product)
        assert product in cart.products
        cart.remove_product(product)
        assert product not in cart.products

    def test_cart_clear(self, product, cart):
        cart.add_product(product, buy_count=2)
        assert cart.products.get(product) == 2
        cart.clear()
        assert cart.products == {}

    def test_cart_get_total_price(self, cart, product):
        cart.add_product(product, 100)
        assert cart.get_total_price() == 100 * 100

    def test_cart_buy(self, product, cart):
        cart.add_product(product, buy_count=2)
        assert cart.products.get(product) == 2
        cart.buy(quantity=2)
        assert cart.products.get(product) == 0