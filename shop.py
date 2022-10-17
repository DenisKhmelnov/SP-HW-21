from BasicStorage import BasicStorage


class Shop(BasicStorage):
    def __init__(self, capacity=20, items={}):
        super().__init__(capacity, items)
        self.max_items = 5

    def add(self, title, qnt):
        if self.get_unique_items_count() == 5 and title not in self.items:
            print("Невозможно добавить больше 5 товаров")
            return False
        return super().add(title, qnt)
