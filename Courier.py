from BasicStorage import BasicStorage
from Request import Request


class Courier:
    def __init__(self, request: Request, storages: dict[str, BasicStorage]):
        self.request = request
        self.departure = storages.get(request.departure)
        self.destination = storages.get(request.destination)

    def move(self):
        item = self.request.item
        amount = self.request.amount

        if self.departure.remove(title=item, qnt=amount):
            print(f"Курьер забрал {amount} {item} из {self.request.departure}")
            if self.destination.add(title=item, qnt=amount):
                print(f"Курьер доставил {amount} {item} в {self.request.destination}")
            #возвращаем товар обратно, если в пункте назначения нет места
            else:
                self.departure.add(title=item, qnt=amount)
                print("Товар возвращен в место отправления")

