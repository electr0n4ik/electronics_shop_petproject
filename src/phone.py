from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim > 0 and isinstance(number_of_sim, int):
            self.sim_count = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        if isinstance(other, Phone) or isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return None
