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
