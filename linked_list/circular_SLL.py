class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CircullarLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += '->'
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return result

    def createCLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        self.length = 1

    def prepend(self, value):
        if self.head == None:
            self.createCLL(value)
            return "created new CLL"
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
            self.length += 1

    def append(self, value):
        if self.head == None:
            self.createCLL(value)
            return "created new CLL"
        else:
            newNode = Node(value)
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def insertAtAnyLocation(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index == -1 or index == self.length:
            self.append(value)
        elif index < -1 or index > self.length:
            return "Index is invalid"
        else:
            newNode = Node(value)
            tempNode = self.head
            tempIndex = 0
            while tempIndex < index -1:
                tempNode = tempNode.next
                tempIndex += 1
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode
            self.length += 1
    
    def traversal(self):
        if self.head is None:
            return "first create a CLL"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
        
    def searchByValue(self, value):
        if self.head is None:
            return "first create a CLL"
        else:
            tempNode = self.head
            index = 0
            while tempNode:
                if tempNode.value == value:
                    return index
                else:
                    tempNode = tempNode.next
                    index += 1
                if tempNode == self.tail.next:
                    break


    def searchByIndex(self, index):
        if self.head is None:
            return "first create a CLL"
        elif index == 0:
            return self.head
        elif index == -1 or index == self.length:
            return self.tail
        elif index < -1 or index > self.length:
            return "index not valid"
        else:
            tempNode = self.head
            for _ in range(index):
                tempNode = tempNode.next
            return tempNode
        
    def popFirst(self):
        poppedNode = self.head
        if self.head is None:
            return "first create a CLL"
        elif self.head == self.tail:
            self.tail.next = None
            self.head = None
            self.tail = None
            self.length -= 1
            return poppedNode
        else:
            self.head = self.head.next
            self.tail.next = self.head
            self.length -= 1
            return poppedNode
        
    def popLast(self):
        poppedNode = self.tail
        if self.head is None:
            return "first create a CLL"
        elif self.head == self.tail:
            self.tail.next = None
            self.head = None
            self.tail = None
            self.length -= 1
            return poppedNode
        else:
            node = self.head
            while node:
                if node.next == self.tail:
                    break
                node = node.next
            node.next = self.head
            self.tail = node
            self.length -= 1
            return poppedNode
        
    def popAnyIndex(self, index):
        if self.head is None:
            return "first create a CLL"
        elif index == 0:
            self.popFirst()
        elif index == -1 or index == self.length:
            self.popLast()
        elif index < -1 or index > self.length:
            return "Please enter a valid index"
        else:
            tempNode = self.head
            tempIndex = 0
            while tempIndex < index - 1:
                tempNode = tempNode.next
                tempIndex += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next
            self.length -= 1
            return nextNode
        
    def popByValue(self, value):
        if self.head == None:
            return "first create CLL"
        else:
            index = self.searchByValue(value)
            poppedNode = self.popAnyIndex(index)
            self.length -= 1
            return poppedNode
        
    def popAll(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length = 0

newCircularLinkedList = CircullarLinkedList()
newCircularLinkedList.createCLL(3)
print(newCircularLinkedList)
newCircularLinkedList.append(4)
newCircularLinkedList.append(5)
newCircularLinkedList.append(7)
newCircularLinkedList.prepend(2)
newCircularLinkedList.prepend(1)
newCircularLinkedList.prepend(0)
print(newCircularLinkedList)
newCircularLinkedList.insertAtAnyLocation(6,6)
newCircularLinkedList.insertAtAnyLocation(8,8)
print(newCircularLinkedList)
newCircularLinkedList.traversal()
newCircularLinkedList.popFirst()
newCircularLinkedList.popLast()
newCircularLinkedList.popAnyIndex(5)
newCircularLinkedList.popByValue(3)
print(newCircularLinkedList)







            