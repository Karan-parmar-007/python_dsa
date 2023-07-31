class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = list(self.list)
        values.reverse()
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def check_if_empty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def check_is_full(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self ,value):
        if self.check_is_full():
            return "stack is already full"
        else:
            self.list.append(value)
            return "pushed successfully"

    def pop(self):
        if self.check_if_empty():
            return "stack is already empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.check_if_empty():
            return "stack is already empty"
        else:
            return self.list[len(self.list) - 1]
        
    def delete(self):
        self.list = None

my_stack = Stack(7)
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
