from storage import Storage


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value


    def add(self, title, qnt):
        if self.capacity == 0:
            print("На складе нет места")
        elif self.get_free_space() >= qnt:  # проверяем, что места достаточно
            if self.items.get(title):
                self.items[title] += qnt
            else:
                self.items[title] = qnt  # добавляем новый товар
            self.capacity -= qnt  # уменьшаем свободное место
        else:  # если места на весь товар недостаточно
            if self.items.get(title):
                self.items[title] += self.capacity
            else:
                self.items[title] = self.capacity
            self.capacity = 0

    def remove(self, title, qnt):
        if self.items.get(title):
            if self.items[title] >= qnt:
                self.items[title] -= qnt
                self.capacity += qnt
            else:
                self.capacity += self.items.pop(title) #обнуляем количество товара и удаляем его из словаря
        else:
            print("Нет такого товара")

    def get_free_space(self):
        return self.capacity

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)
