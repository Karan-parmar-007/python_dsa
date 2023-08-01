class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        tempNode = self.head
        result  = ''
        while tempNode:
            result += str(tempNode.value)
            if tempNode.next:
                result += '->'
            tempNode = tempNode.next
        return result

    def create(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length += 1

    def append(self, value):
        if self.length == 0:
            self.create(value)
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
    
    def prepend(self, value):
        if self.length == 0:
            self.create(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            self.length += 1

    def insertAtAnyPoint(self,index,value):
        if index == 1:
            self.prepend(value)
        elif index == self.length or index == -1:
            self.append(value)
        elif index > self.length or index < -1:
            return "index is incorrect"
        else:
            newNode = Node(value)
            tempNode = self.head
            for _ in range(index -1):
                tempNode = tempNode.next
            newNode.next = tempNode.next
            tempNode.next = newNode
            self.length += 1

    def traversal(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next

    def searchByValue(self, target):
        currentNode = self.head
        index = 0
        while currentNode:
            if currentNode.value == target:
                return index
            else:
                currentNode = currentNode.next
                index += 1
            

    def searchByIndex(self, index):
        if index == -1 or index == self.length:
            return self.tail
        elif index == 1:
            return self.head
        elif index > self.length or index < -1:
            return "wrong index value"
        else:
            currentNode = self.head
            for _ in range(index):
                currentNode = currentNode.next
            return currentNode

    def popFirstElement(self):
        poppedNode = self.head
        if self.length == 0 or self.length <= -1:
            return "SLL do not exist"
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return poppedNode
        else:
            self.head = self.head.next
            poppedNode.next = None
            self.length -= 1
            return poppedNode

    def popLastElement(self):
        poppedNode = self.tail
        if self.length == 0 or self.length <= -1:
            return "SLL do not exist"
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return poppedNode
        else:
            tempNode = self.head
            while tempNode.next:
                tempNode = tempNode.next
            self.tail = tempNode
            tempNode.next = None
            self.length -= 1
            return poppedNode
    
    def popAtIndex(self, index):
        if index == 1:
            self.popFirstElement()
        elif index == -1 or index == self.length:
            self.popLastElement()
        elif index < -1 or index > self.length:
            return "index is not correct"
        else:
            prevNode = self.searchByIndex(index - 1)
            poppedNode = prevNode.next
            prevNode.next = poppedNode.next
            poppedNode.next = None
            self.length -= 1
            return poppedNode

    def popElementByValue(self, value):
        index = self.searchByValue(value)
        poppedNode = self.popAtIndex(index)
        return poppedNode
    
    def popAll(self):
        self.head = None
        self.tail = None
        self.length = 0

newLinkedList = LinkedList()
newLinkedList.create(4) 
newLinkedList.prepend(3)
newLinkedList.prepend(1)
newLinkedList.prepend(0)
newLinkedList.append(5)
newLinkedList.append(6)
newLinkedList.append(8)
print(newLinkedList)
newLinkedList.insertAtAnyPoint(2,2)
newLinkedList.insertAtAnyPoint(7,7)
print(newLinkedList)
newLinkedList.traversal()
newLinkedList.popFirstElement()
newLinkedList.popLastElement()
print(newLinkedList)
newLinkedList.popAtIndex(3)
print(newLinkedList)
newLinkedList.popElementByValue(7)
print(newLinkedList)
newLinkedList.popAll()
print(newLinkedList)