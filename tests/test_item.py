from src.item import Item

item_1 = Item("Name", 100, 200)
def test_item():
    assert  item_1.name == "Name"
    assert  item_1.price == 100
    assert item_1.quantity == 200
