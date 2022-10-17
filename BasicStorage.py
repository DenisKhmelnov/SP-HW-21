from storage import Storage


class BasicStorage(Storage):
    def __init__(self, capacity, items={}):
        self._items = items
        self._capacity = capacity

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
        if self.get_free_space() == 0:
            print("На складе нет места")
            return False
        elif self.get_free_space() >= qnt:  # проверяем, что места достаточно
            if self.items.get(title):
                self.items[title] += qnt
            else:
                self.items[title] = qnt  # добавляем новый товар
            return True
        else:  # если места на весь товар недостаточно
            print("Недостаточно места, что бы сохранить всю партию")
            return False

    def remove(self, title, qnt):
        if self.items.get(title):
            if self.items[title] >= qnt:
                self.items[title] -= qnt
                if self.items[title] == 0: #удаляем товар со склада, если его по нулям
                    self.items.pop(title)
                return True
            else:
                print("Не хватает запрашиваемого количества товара")
                return False
        else:
            print("Нет такого товара")
            return False

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)