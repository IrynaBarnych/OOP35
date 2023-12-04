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


