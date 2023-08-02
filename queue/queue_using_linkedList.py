class Node:
    def __init__(self, value= None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        value = [str(x) for x in self.linkedList]
        return '  '.join(value)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.isEmpty():
            return "The Queue is already  Empty"
        elif self.linkedList.head == self.linkedList.tail:
            dequeuedItem = self.linkedList.head
            self.linkedList.head = None
            self.linkedList.tail = None
            return dequeuedItem
        else:
            dequeuedItem = self.linkedList.head
            self.linkedList.head = self.linkedList.head.next
            return dequeuedItem
        
    def peek(self):
        if self.isEmpty():
            return "There is no element in list"
        else:
            return self.linkedList.head
        
    def delete(self):
        if self.isEmpty():
            return "already Empty"
        else:
            self.linkedList.head = None
            self .linkedList.tail = None
            return "Successfully deleted"
        
newQueue = Queue()
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
print(newQueue)
print(newQueue.peek())
newQueue.delete()
print(newQueue)