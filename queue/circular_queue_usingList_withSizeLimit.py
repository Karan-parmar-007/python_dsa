class Queue:
    def __init__(self, maxSize):
        self.item = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        value = [str(x) for x in self.item]
        return '  '.join(value)
    
    def isFull(self):
        if self.top+1 == self.start:
            return True
        elif self.start == 0 and self.top+1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if self.isFull():
            return "queue is full"
        else:
            self.top += 1
            if self.start == 0:
                self.start = 0
            else:
                self.start += 1

        self.item[self.top] = value
        return "element added successfully"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            firstElement = self.item[self.start]
            start = self.start
            if self.start == self.top:
                self.start -= 1
                self.top -= 1
            elif self.start+1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.item[start] = None
            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return "Queue is emplty"
        else:
            return self.item[self.start]
        
    def delete(self):
        self.item = self.maxSize * [None]
        self.top = -1
        self.start  = -1

newQueue = Queue(5)
newQueue.enqueue(1)
newQueue.enqueue(2)
newQueue.enqueue(3)
newQueue.enqueue(4)
newQueue.enqueue(5)
newQueue.enqueue(6)
print(newQueue)
newQueue.dequeue()
newQueue.dequeue()
newQueue.dequeue()
newQueue.dequeue()
print(newQueue)
newQueue.peek()
newQueue.delete()
print(newQueue)