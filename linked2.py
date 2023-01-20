class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
    
    def print_tail(self):
        current_tail = self.tail.value
        print(current_tail)

myLink = LinkedList(10)
myLink.append(25)
myLink.append(52)
myLink.prepend(15)
# myLink.print_list()

list2 = [1,2,3,5,6,879,36]

for i in range(len(list2)):
    myLink.prepend(list2[i])

# myLink.print_list()
myLink.print_tail()