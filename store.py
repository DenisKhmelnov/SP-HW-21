from storage import Storage

class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100


    def get_free_space(self):
        return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)