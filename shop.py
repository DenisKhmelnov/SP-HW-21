from store import Store

class Shop(Store):

    def __init__(self):
        self._items = {}
        self._capacity = 20
        self._items_count = 0

    @property
    def items(self):
        return self._items

    @property
    def items_count(self):
        return self._items_count

    @items_count.setter
    def items_count(self, value):
        self._items_count = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value


    def add(self, title, qnt):
        if self.capacity == 0:
            print("В магазине нет места")
        elif self.get_free_space() >= qnt:  # проверяем, что места достаточно
            if self.items.get(title):
                self.items[title] += qnt
            else:
                if self.items_count == 5:
                    print("В магазине не может быть больше 5 видов товара")
                    return False
                self.items[title] = qnt  # добавляем новый товар
                self.items_count += 1
            self.capacity -= qnt  # уменьшаем свободное место
        else:  # если места на весь товар недостаточно
            if self.items.get(title):
                self.items[title] += self.capacity
            else:
                self.items[title] = self.capacity
            self.capacity = 0

    def remove(self, title, qnt):
        if self.items.get(title):
            if self.items[title] > qnt:
                self.items[title] -= qnt
                self.capacity += qnt
            else:
                self.capacity += self.items.pop(title)
                self.items_count -= 1
        else:
            print("Нет такого товара")

    def get_free_space(self):
        return self.capacity

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)


shop = Shop()
shop.add("cocain", 5)
shop.add("heroin", 3)
shop.remove("heroin", 3)
print(shop.items_count)