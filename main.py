# Завдання 1
# Розробіть додаток, що імітує чергу запитів до сервера.
# Мають бути клієнти, які надсилають запити на сервер, кожен
# з яких має свій пріоритет. Кожен новий клієнт потрапляє у
# чергу залежно від свого пріоритету. Зберігайте статистику
# запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.

import datetime
from collections import deque


class Request:
    def __init__(self, user_login, priority):
        self.user_login = user_login
        self.priority = priority
        self.timestamp = None


class ServerQueue:
    def __init__(self):
        self.request_queue = deque()
        self.stats_queue = []

    def add_request(self, user_login, priority):
        request = Request(user_login, priority)
        self.request_queue.append(request)
        print(f"Запит від користувача {user_login} додано до черги з пріоритетом {priority}.")

    def process_requests(self):
        if not self.request_queue:
            print("Черга запитів порожня.")
            return

        timestamp = datetime.datetime.now()
        self.request_queue = deque(sorted(self.request_queue, key=lambda x: x.priority))

        for request in self.request_queue:
            request.timestamp = timestamp
            self.stats_queue.append((request.user_login, timestamp))
            print(
                f"Обробка запиту від користувача {request.user_login} з часом {timestamp} та пріоритетом {request.priority}.")

        self.request_queue.clear()

    def display_stats(self):
        print("\nСтатистика запитів:")
        for user_login, timestamp in self.stats_queue:
            print(f"Користувач {user_login}: {timestamp}")


# Приклад використання:
server = ServerQueue()
server.add_request("user1", 2)
server.add_request("user2", 1)
server.add_request("user3", 3)

server.process_requests()
server.display_stats()

# gpt-чат порекомендував додати бібліотеки