from src.item import Item
from src.phone import Phone
import pytest

phone_1 = Phone("Iphone 15", 150_000, 3, 2)
phone_2 = Phone("Iphone 15", 150_000, 5, 2)
item_1 = Item("Клавиатура", 800, 15)


def test_phone_attr():

    assert phone_1.name == "Iphone 15"
    assert phone_1.price == 150_000
    assert phone_1.quantity == 3
    assert phone_1.number_of_sim == 2


def test_add():
    print(phone_1 + phone_2)
    assert phone_1 + phone_2 == 8
    assert phone_1 + item_1 == 18
    assert phone_1 + 1 == None


def test_item_repr():

    assert repr(phone_2) == "Phone('Iphone 15', 150000, 5, 2)"


def test_item_str():

    assert str(phone_2) == "Iphone 15"

