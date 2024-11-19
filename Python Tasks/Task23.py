class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)

    def remove(self):
        if not self.queue:
            return "The queue is empty"
        return self.queue.pop(0)

queue = Queue()
queue.insert(5)
queue.insert(6)
print(queue.remove()) 
queue.insert(7)
print(queue.remove())  
print(queue.remove())  
print(queue.remove())  