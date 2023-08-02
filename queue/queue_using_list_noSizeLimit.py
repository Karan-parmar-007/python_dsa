class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ''.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "added successfully"
    
    def dequeue(self):
        if self.isEmpty() == True:
            return "Queue is already empty"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None

newQueue = Queue()
newQueue.enqueue(1)
newQueue.enqueue(2)
newQueue.enqueue(3)
newQueue.enqueue(4)
newQueue.enqueue(5)
print(newQueue)
newQueue.dequeue()
newQueue.dequeue()
newQueue.dequeue()
newQueue.dequeue()
print(newQueue)
print(newQueue.peek())
newQueue.delete()