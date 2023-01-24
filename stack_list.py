class Stack:
    def __init__(self):
        self.list = list()
        self.length = 0
    
    def peek(self):
        if self.length == 0:
            return None
        return self.list[self.length-1]

    def push(self, value):
        self.list.append(value)
        self.length += 1
    
    def pop(self):
        self.list.pop()
        self.length -= 1
    

my_stack = Stack()

my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
my_stack.push('d')

my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()

print(my_stack.list)
print(my_stack.length)
print(my_stack.peek())
