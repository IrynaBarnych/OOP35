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

def main():
    user_db = Dodatok()

    while True:
        print("\nОберіть операцію:")
        print("1. Додати нового користувача")
        print("2. Видалити існуючого користувача")
        print("3. Перевірити, чи існує такий користувач")
        print("4. Змінити логін існуючого користувача")
        print("5. Змінити пароль існуючого користувача")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            login = input("Введіть логін: ")
            password = input("Введіть пароль: ")
            user_db.add_user(login, password)
        elif choice == "2":
            login = input("Введіть логін користувача, якого потрібно видалити: ")
            user_db.remove_user(login)
        elif choice == "3":
            login = input("Введіть логін користувача для перевірки: ")
            user_db.check_user(login)
        elif choice == "4":
            old_login = input("Введіть старий логін користувача: ")
            new_login = input("Введіть новий логін користувача: ")
            user_db.change_login(old_login, new_login)
        elif choice == "5":
            login = input("Введіть логін користувача, пароль якого потрібно змінити: ")
            new_password = input("Введіть новий пароль: ")
            user_db.change_password(login, new_password)
        elif choice == "0":
            print("Дякую за використання додатку. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
