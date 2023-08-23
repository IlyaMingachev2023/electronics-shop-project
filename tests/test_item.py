from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
def test_calculate_total_price():
    assert item1.price * item1.quantity == 200000


def test_calculate_total_price():
    assert item2.price * item2.quantity == 100000

def test_apply_discount():
    pay_rate = 1.0
    item1.price = item1.price * pay_rate
    assert item1.price == 10000

def test_apply_discount():
    pay_rate = 0.8
    item2.price = item2.price * pay_rate
    assert item2.price == 16000