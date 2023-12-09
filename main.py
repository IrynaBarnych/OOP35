# Завдання 2
# Створіть імітаційну модель «Причал морських катерів».
# Введіть таку інформацію:
# 1. Середній час між появою пасажирів на причалі у різний
# час доби;
# 2. Середній час між появою катерів на причалі у різний час
# доби;
# 3. Тип зупинки катера (кінцева або інша).
# Визначіть:
# 1. Середній час перебування людини на зупинці;
# 2. Достатній інтервал часу між приходами катерів, коли на
# зупинці не більше N людей одночасно;
# 3. Кількість вільних місць у катері є випадковою величиною.
# Вибір необхідних структур даних визначте самостійно.

from datetime import datetime
import time

class PierPassenger:
    def __init__(self, name):
        self.name = name
        self.arrival_time = time.time()

class SeaBoat:
    def __init__(self, boat_name, stop_type):
        self.boat_name = boat_name
        self.stop_type = stop_type

class PierQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def insert_passenger(self, passenger):
        if not self.is_full():
            self.queue.append(passenger)
            print(f"Пасажир {passenger.name} прибув на причал.")
        else:
            print("Причал повний. Пасажир не може прибути.")

    def pull_passenger(self):
        if not self.is_empty():
            passenger = self.queue.pop(0)
            print(f"Пасажир {passenger.name} відправився з причалу.")
            return passenger
        else:
            print("Причал порожній. Немає пасажира для відправлення.")
            return None

    def show(self):
        if not self.is_empty():
            print("Пасажири на причалі:")
            for passenger in self.queue:
                arrival_time = datetime.fromtimestamp(passenger.arrival_time)
                formatted_time = arrival_time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"Пасажир {passenger.name} прибув о {formatted_time}")
        else:
            print("Причал порожній.")

class SeaBoatSimulator:
    def __init__(self, pier_queue, boat_name, stop_type):
        self.pier_queue = pier_queue
        self.boat = SeaBoat(boat_name, stop_type)

    def simulate_arrival(self):
        if not self.pier_queue.is_empty():
            passenger = self.pier_queue.pull_passenger()
            print(f"{self.boat.boat_name} прибув на причал для {self.boat.stop_type} зупинки.")
            print(f"Пасажир {passenger.name} сів на борт катера {self.boat.boat_name}.")
        else:
            print(f"{self.boat.boat_name} прибув на причал, але пасажирів немає.")

pier_queue = PierQueue(10)

for i in range(1, 11):
    passenger = PierPassenger(f"Пасажир {i}")
    pier_queue.insert_passenger(passenger)

pier_queue.show()

boat1 = SeaBoat("Катер A", "end")
simulator1 = SeaBoatSimulator(pier_queue, "Катер A", "end")
simulator1.simulate_arrival()

boat2 = SeaBoat("Катер B", "other")
simulator2 = SeaBoatSimulator(pier_queue, "Катер B", "other")
simulator2.simulate_arrival()

pier_queue.show()

