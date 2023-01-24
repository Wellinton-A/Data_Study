class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def peek(self):
        return self.top
    
    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node
        self.length += 1
    
    def pop(self):
        if self.top == None:
            return self.top
        data = self.top.data
        self.top = self.top.next
        self.length -= 1
        return data
            

    def is_empty(self):
        return self.top == None
            

myStack = Stack()
myStack.push("Google")
myStack.push("Udemy")
myStack.push("Discord")

myStack.pop()
myStack.pop()





print(myStack.top)
