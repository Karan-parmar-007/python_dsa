class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.Tail = None
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

    def createDLL(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        self.length +=1
        return "DLL is created successfully"

    def insert_start(self, value):
        if self.head is None:
            self.createDLL(value)
            return "created new DLL"
        else:
            newNode = Node(value)
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.length += 1

    def insert_end(self, value):
        if self.head is None:
            self.createDLL(value)
            return "created new DLL"
        else:
            newNode = Node(value)
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def insert(self, value, location):
        if self.head is None:
            self.createDLL(value)
            return "created new DLL"
        elif location == 0:
            self.insert_start(value)
            return "inserted at start"
        elif location == self.length or location == -1:
            self.insert_end(value)
            return "inserted at end"
        elif location < -1 or location >= self.length:
            return "please check the location and try again"
        else:
            newNode = Node(value)
            temp = self.head
            index = 0
            while index == location - 1:
                temp = temp.next
                index += 1
            newNode.next = temp.next
            newNode.prev = temp
            newNode.next.prev = newNode
            temp.next = newNode
            self.length += 1
            return "successfully inserted"

    def traverseDLL(self):
        if self.head is None:
            return "first create a DLL"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def revTraverseDLL(self):
        if self.head is None:
            return "first create a DLL"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev        

# enter the index of which you want to know the value of            
    def search_index(self, index):
        if self.head is None:
            return " create the DLL first"
        elif index == 0:
            return self.head
        elif index == -1 or index == self.length:
            return self.tail
        elif index < -1 or index >= self.length:
            return "check the index value beacuse it is not present in the DLL"
        else:
            loc = 0
            tempNode = self.head
            while loc < index:
                tempNode = tempNode.next
                loc += 1
            return tempNode
        
# check if value is present or not and if present that at which index
    def search_value(self, value):
        if self.head is None:
            return "create DLL first."
        else:
            tempNode = self.head
            index = 0
            while tempNode:
                if tempNode.value == value:
                    return index
                tempNode = tempNode.next
                index += 1
            return "Node is not present"
    
    def pop_first(self):
        if self.head is None:
            return "create DLL first."
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.head = self.head.next 
            self.head.prev = None
            self.length -= 1 
    
    def pop_last(self):
        if self.head is None:
            return "create DLL first."
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

    def pop_any(self, index):
        if self.head is None:
            return "create DLL first."
        elif index == 1:
            self.pop_first()
        elif index == -1 or index == self.length:
            self.pop_last()
        elif index < -1 or index >= self.length:
            return "please enter the index properly because this index dose not exist"
        else:
            tempNode = self.head
            loc = 0
            while loc < index - 1:
                tempNode = tempNode.next
                loc += 1
            tempNode.next = tempNode.next.next
            tempNode.next.prev = tempNode
            self.length -= 1

    def pop_value(self, value):
        if self.head is None:
            return "create DLL first."
        else:
            index = self.search_value(value)
            if index == "Node is not present":
                return "Node is not present"
            else:
                self.pop_any(index)

    def delDLL(self):
        if self.head is None:
            return "create DLL first."
        else:
            current = self.head
            while current:
                next_node = current.next
                current.prev = None
                current.next = None
                current = next_node
            self.head = None
            self.tail = None
            self.length = 0
            return "DLL deleted successfully"


new_dll = DoublyLinkedList()
new_dll.createDLL(3)
new_dll.insert_start(2)
new_dll.insert_start(1)
new_dll.insert(0,0)
new_dll.insert_end(4)
new_dll.insert_end(5)
new_dll.insert(6,6)
print(new_dll)
print(new_dll.search_index(4).value)
print(new_dll.search_value(5))
new_dll.pop_first()
new_dll.pop_last()
print(new_dll)
new_dll.pop_any(3)
new_dll.pop_value(2)
print(new_dll)
new_dll.delDLL()
print(new_dll)
