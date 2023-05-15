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
    assert item_1.apply_discount(10) == 90
    assert print(item_1.instantiate_from_csv()) == list_objects
    assert Item.string_to_number("ff 100") == 100
