class Request:
    def __init__(self, storages:dict, request:str):

        split_instruction = request.split(" ")
        self.storages = storages
        self.amount = int(split_instruction[1])
        self.item = split_instruction[2]
        self.departure = split_instruction[4]
        self.destination = split_instruction[6]

        if self.departure not in storages or self.destination not in storages:
            print("Пункт отправки или доставки выбран неверно")





