from Courier import Courier
from Request import Request
from shop import Shop
from store import Store

shop = Shop(items={'масло': 5,
                   'орехи': 5,
                   'специи': 3,
                   'молоко': 4},
            capacity=20)
store = Store(items={'картошка': 10,
                     'макароны': 15,
                     'специи': 20,
                     'финики': 10,
                     'консервы': 15}, capacity=100)

storages = {
    "магазин": shop,
    "склад": store,
}

while True:
    # вывести что хранится в storages
    for storage, items in storages.items():
        print(f"В {storage} содержится {items.items}")

    # обработать ввод пользователя
    print("Введите стоп, stop, что бы завершить программу, либо введите запрос.")
    request = input("Введите свой запрос в формате: Доставить 3 собачки из склад в магазин:")

    if request in ("stop", "стоп"):
        break
    request_obj = Request(storages=storages, request=request)

    # выполнить перемещение
    courier = Courier(request=request_obj, storages=storages)
    courier.move()
