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

    def enqueue(self, item, priority):
        if not self.is_full():
            self.queue.append((item, priority))
            print(f"Елемент {item} з пріорітетом {priority} додано до черги")

    def dequeue(self):
        if not self.is_empty():
            item, priority = self.queue.pop(0)
            print(f"Елемент {item} з пріорітетом {priority} вилучено з черги")

    def show(self):
        if not self.is_empty():
            print("Елементи в черзі")
            for item, priority in self.queue:
                print(f"Елемент {item} з {priority}-пріорітетом")
        else:
            print("Черга порожня")

# Додано меню
def main():
    capacity = int(input("Введіть максимальну кількість елементів у черзі: "))
    q = PriorityQueue(capacity)

    while True:
        print("\nОберіть операцію:")
        print("1. Додати елемент з пріоритетом")
        print("2. Вилучити елемент з найвищим пріоритетом")
        print("3. Переглянути найбільший за пріоритетом елемент")
        print("4. Переглянути всі елементи черги")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            item = input("Введіть елемент: ")
            priority = int(input("Введіть пріоритет: "))
            q.insert_with_priority(item, priority)
        elif choice == "2":
            enqueue()
        elif choice == "3":
            q.peek()
        elif choice == "4":
            q.show()
        elif choice == "0":
            print("Дякую за використання черги з пріоритетами. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
