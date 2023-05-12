class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, __name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param __name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = __name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter  # property-name.setter decorator
    def name(self, value):
        if len(value) < 10:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self, percent):
        """
        Применяет установленную скидку для конкретного товара.
        """
        cur_price = self.price - self.price * (percent / 100)
        # из-за того, что следующая строка не прошла flake8 я оставил конечную цену с учетом скидки без текста
        # str_result = f"Стоимость товара с учетом скидки в {percent}% будет -> {cur_price}"
        return cur_price

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
            return False
        else:
            return float(str_numbers)



