from src.item import Item

Orange = Item("Orange", 105, 10)

if __name__ == "__main__":
    print(Orange.name)
    print(Orange.apply_discount(10))
