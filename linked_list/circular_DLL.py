class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
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


    def createCDLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        self.length += 1
        return "Created successfully"
    
    def insert_start(self, value):
        if self.head is None:
            self.createCDLL(value)
            return "since there was no CDLL we created one enjoy!"
        else:
            newNode = Node(value)
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.head = newNode
            self.tail.next = newNode
            self.length += 1
            return "added to start"
        
    def insert_end(self, value):
        if self.head is None:
            self.createCDLL(value)
            return "since there was no CDLL we created one enjoy!"
        else:
            newNode = Node(value)
            newNode.prev = self.tail
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
            self.head.prev = newNode
            self.length += 1
            return "Added to end"

    def insert_any(self, value, location):
        if self.head is None:
            self.createCDLL(value)
            return "since there was no CDLL we created one enjoy!"
        elif location == 0:
            self.insert_start(value)
        elif location == -1 or location == self.length:
            self.insert_end(value)
        elif location < -1 or location >= self.length:
            return "check the location"
        else:
            newNode = Node(value)
            tempNode = self.head
            index = 0
            while index < location-1:
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next
            newNode.prev = tempNode
            newNode.next.prev = newNode
            tempNode.next = newNode
            return "Inserted successfully"

    def traversal_in_CDLL(self):
        if self.head is None:
            return "please create the CDLL first"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def revtraversal_in_CDLL(self):
        if self.head is None:
            return "please create the CDLL first"
        else:
            tempNode = self.tail
            while tempNode:
                print (tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev 

    def search_index(self ,index):
        if self.head is None:
            return "please create the CDLL first"
        else:
            tempNode = self.head
            loc = 0
            while loc < index:
                tempNode = tempNode.next
                loc += 1
            return tempNode.value

    def search_value(self, value):
        if self.head is None:
            return "please create the CDLL first"

        else:
            tempNode = self.head
            loc = 0
            while tempNode:
                if tempNode.value == value:
                    return f"the value is present at index {loc}"
                elif tempNode  == self.tail:
                    return "The value is not present"
                else:
                    tempNode = tempNode.next
                    loc += 1
    def del_start(self):
        if self.head is None:
            return "please create the CDLL first"
        else:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None
                self.length -= 1
                return "deleted"
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
                self.length -= 1
                return "deleted"

    def del_end(self):
        if self.head is None:
            return "please create the CDLL first"
        else:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None
                self.length -= 1
                return "deleted"
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
                self.length -= 1
                return "deleted"

    def del_any(self ,index):
        if self.head is None:
            return "please create the CDLL first"
        elif index == 0:
            self.del_start()
        elif index == -1 or index == self.length:
            self.del_end()
        elif index < -1 or index >= self.length:
            return f"please check the index the minimum allowed value is 0 and maximum is {self.length}"
        else:
            tempNode = self.head
            loc = 0
            while loc < index - 1:
                tempNode = tempNode.next
                loc += 1
            tempNode.next = tempNode.next.next
            tempNode.next.prev = tempNode
            return "deleted"
        
    def del_all(self):
        if self.head is None:
            return "please create the CDLL first"
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            return "deleted all your efforts :( "
    
    def len_of_CDLL(self):
        return self.length

new_CDLL = CircularDoublyLinkedList()
new_CDLL.createCDLL(2)
new_CDLL.insert_start(1)
new_CDLL.insert_start(0)
print(new_CDLL)
print(new_CDLL.len_of_CDLL())
new_CDLL.insert_end(3)
new_CDLL.insert_end(5)
new_CDLL.insert_any(4,4)
print(new_CDLL)
print(new_CDLL.search_index(4))
print(new_CDLL.search_value(6))
new_CDLL.revtraversal_in_CDLL()
new_CDLL.del_any(0)
new_CDLL.del_any(4)
new_CDLL.del_end()
print(new_CDLL)
new_CDLL.del_all()
print(new_CDLL)
 

        