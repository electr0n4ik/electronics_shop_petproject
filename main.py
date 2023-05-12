from src.item import Item

Orange = Item("Orange", 110, 10)

if __name__ == "__main__":
    print(Orange.name)
    print(Orange.apply_discount(10))
    print()
    print(Item.instantiate_from_csv())
    print(Item.string_to_number("ff 100"))
    print()
    for i in Item.instantiate_from_csv():
        print(i.name, i.price, i.quantity)
