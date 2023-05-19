from src.item import Item
import pytest

item_1 = Item("Name", 100, 200)
list_objects = """[<src.item.Item object at 0x7f94ad4cb390>, 
<src.item.Item object at 0x7f94ad4cb350>, 
<src.item.Item object at 0x7f94ad4cb410>, 
<src.item.Item object at 0x7f94ad4cb450>, 
<src.item.Item object at 0x7f94ad4cb4d0>]"""


def test_item():
    assert item_1.name == "Name"
    assert item_1.price == 100
    assert item_1.quantity == 200
    # assert item_1.name("Транзистор") == "Транзистор"
    assert item_1.calculate_total_price() == 100 * 200

    Item.pay_rate = 0.8
    item_1.apply_discount()
    assert item_1.price == 80
    # assert print(item_1.instantiate_from_csv()) == list_objects
    assert Item.string_to_number("ff 100") == 100


def test_item_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item(name=Смартфон, price=10000, quantity=20)"


def test_item_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == "Item: Смартфон, Price: 10000, Quantity: 20"
