#черга через список
queue = []
queue.append("a")
queue.append("b")
queue.append("c")
print(queue)
queue.append(queue.pop(0)) #кругова черга (Ring Buffer)
print(queue)


