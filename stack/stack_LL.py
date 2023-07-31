class Node:
    def __init__(self ,value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            node = node.next

class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        temp_node = self.linkedList.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += '->'
            temp_node = temp_node.next
        return result

    
    def check_is_empty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
        
    def push(self ,value):
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node

    def pop(self):
        if self.check_is_empty():
            return "already empty"
        else:
            nodeValue = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.check_is_empty():
            return "already empty"
        else:
            nodeValue = self.linkedList.head.value
            return nodeValue

    def delete(self):
        self.linkedList.head = None

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.push(4))
print(my_stack.peek())
print("--------------------------------")
print(my_stack)
print("--------------------------------")
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack)        
    