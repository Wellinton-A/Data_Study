class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def peek(self):
        if self.head == None:
            return self.head
        return self.head.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    def dequeue(self):
        if self.is_empty():
            return
        self.head = self.head.next
        self.length -= 1
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        return self.length

my_queue = Queue()
my_queue.enqueue('a')
my_queue.enqueue('b')
my_queue.enqueue('c')
my_queue.enqueue('d')
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.peek())
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.dequeue()
print(my_queue.peek())