"""Завдання 2
Створіть клас черги з пріоритетами для роботи із
символьними значеннями.
Ви маєте створити реалізації для операцій над елементами черги:
■ IsEmpty — перевірка, чи черга пуста;
■ IsFull — перевірка черги на заповнення;
■ InsertWithPriority — додати елемент з пріоритетом у
чергу;
 PullHighestPriorityElement — видалення елемента з
найвищим пріоритетом із черги;
■ Peek — повернення найбільшого за пріоритетом елемента.
 Зверніть увагу, що елемент не видаляється з
черги;
■ Show — відображення на екрані всіх елементів черги.
Показуючи елемент, також необхідно вказати і його
пріоритет.
На старті додатка відобразіть меню, в якому користувач
 може вибрати необхідну операцію."""
class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def insert_with_priority(self, item, priority):
        if not self.is_full():
            self.queue.append((item, priority))
            print(f"Елемент {item} з пріорітетом {priority} додано до черги")
            self.queue.sort(key=lambda x: x[1])
        else:
            print("Черга заповнена")

    def pull_highest_priority_element(self):
        if not self.is_empty():
            item, priority = self.queue.pop(0)
            print(f"Елемент {item} з пріорітетом {priority} вилучено з черги")
        else:
            print("Черга порожня")

    def peek(self):
        if not self.is_empty():
            item, priority = self.queue[0]
            print(f"Найбільший за пріорітетом {priority} елемент {item}")
        else:
            print("Черга порожня")

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
            q.pull_highest_priority_element()
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
