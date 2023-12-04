#черга через список
queue = []
queue.append("a")
queue.append("b")
queue.append("c")
print(queue)
queue.append(queue.pop(0)) #кругова черга (Ring Buffer)
print(queue)


#черга через бібліотеку колекції
from collections import deque
q = deque()

q.append("a")
q.append("b")
q.append("c")
print(q)
q.popleft()
q.popleft()
q.popleft()
q.rotate(2)
print(q)

#черга через бібліотеку queue
from queue import Queue
q = Queue(maxsize=3)
print(q.qsize())
q.put("a")
q.put("b")
q.put("c")
q.put("d")
print(q.queue)
print(q.qsize())

#черга через класи
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "queue is empty"

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "queue is empty"

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.queue)
q.dequeue()
print(q.queue)
print(q.size())

#черга через зв'язаний список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp.data

    def size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        return count

# Приклад використання черги на основі зв'язаного списку:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)

print("Dequeue:", q.dequeue())  # Видалення елемента з черги
print("Size of the queue:", q.size())  # Розмір черги

