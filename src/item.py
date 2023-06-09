

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, __name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param __name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = __name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)  # Добавление экземпляра в список all при создании

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"

    def __str__(self):
        result = f"Item: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return result

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError

    @property
    def name(self):
        return self.__name

    @name.setter  # property-name.setter decorator
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate  # Умножение цены на pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        import csv
        items = []
        with open("src/items.csv", encoding="cp1251") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                price = float(row["price"])
                quantity = int(row["quantity"])
                item = cls(name, price, quantity)
                items.append(item)
        return items

    @staticmethod
    def string_to_number(string):
        str_numbers = ""
        for i in string:
            if i.isdigit():
                str_numbers += i
        if str_numbers == "":
            return 0.0
        else:
            return float(str_numbers)
