# Завдання 3
# Розробіть додаток, який дозволяє зберігати інформацію
# про логіни і паролі користувачів. Кожному користувачеві
# відповідає пара «логін — пароль». При старті додатку
# відображається меню:
# ■ Додати нового користувача;
# ■ Видалити існуючого користувача;
# ■ Перевірити, чи існує такий користувач;
# ■ Змінити логін існуючого користувача;
# ■ Змінити пароль існуючого користувача.
# Для реалізації завдання обов’язково застосуйте одну
# із структур даних. При виборі структури керуйтеся постановкою завдання.

class Dodatok:
    def __init__(self):
        self.users = {}

    def add_user(self, login, password):
        if login in self.users:
            print(f"Користувач з логіном {login} вже існує.")
        else:
            self.users[login] = password
            print(f"Користувача {login} додано з паролем {password}.")

    def remove_user(self, login):
        if login in self.users:
            del self.users[login]
            print(f"Користувача {login} видалено.")
        else:
            print(f"Користувача з логіном {login} не існує.")

    def check_user(self, login):
        if login in self.users:
            print(f"Користувач {login} існує.")
        else:
            print(f"Користувача з логіном {login} не знайдено.")

    def change_login(self, old_login, new_login):
        if old_login in self.users:
            password = self.users.pop(old_login)
            self.users[new_login] = password
            print(f"Логін користувача {old_login} змінено на {new_login}.")
        else:
            print(f"Користувача з логіном {old_login} не знайдено.")

    def change_password(self, login, new_password):
        if login in self.users:
            self.users[login] = new_password
            print(f"Пароль користувача {login} змінено на {new_password}.")
        else:
            print(f"Користувача з логіном {login} не знайдено.")

