# Завдання 1
# Створіть клас черги для роботи із символьними значеннями. Ви маєте створити реалізації для операцій над
# елементами:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ Enqueue — додати новий елемент до черги;
# ■ Dequeue — видалення елемента з черги;
# ■ Show — відображення на екрані всіх елементів черги.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.


class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def enqueue(self, item):
        if not self.is_full():
            priority = int(input("Введіть пріорітет: "))
            self.queue.append((item, priority))
            print(f"Елемент {item} з пріорітетом {priority} додано до черги")
        else:
            print("Черга вже заповнена. Неможливо додати новий елемент.")

    def dequeue(self):
        if not self.is_empty():
            item, priority = self.queue.pop(0)
            print(f"Елемент {item} з пріорітетом {priority} вилучено з черги")
        else:
            print("Черга порожня. Неможливо вилучити елемент.")

    def show(self):
        if not self.is_empty():
            print("Елементи в черзі:")
            for item, priority in self.queue:
                print(f"Елемент {item} з пріорітетом {priority}")
        else:
            print("Черга порожня")

def main():
    capacity = int(input("Введіть максимальну кількість елементів у черзі: "))
    q = PriorityQueue(capacity)

    while True:
        print("\nОберіть операцію:")
        print("1. Додати новий елемент до черги")
        print("2. Видалити елемент з черги")
        print("3. Перевірити, чи черга порожня")
        print("4. Перевірити, чи черга заповнена")
        print("5. Відобразити всі елементи черги")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            item = input("Введіть елемент: ")
            q.enqueue(item)
        elif choice == "2":
            q.dequeue()
        elif choice == "3":
            print(f"Черга порожня: {q.is_empty()}")
        elif choice == "4":
            print(f"Черга заповнена: {q.is_full()}")
        elif choice == "5":
            q.show()
        elif choice == "0":
            print("Дякую за використання черги. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
