class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    
    def append(self, value):
        new_node = Node(value)
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        self.length += 1

    def print_list(self):
        list_nodes = []
        current_node = self.head
        while current_node != None:
            list_nodes.append(current_node.value)
            current_node = current_node.next
        return print(list_nodes)

    
myLink = LinkedList(3)
myLink.append(4)
myLink.append(5)
myLink.prepend(2)
myLink.prepend(1)

list1 = list(range(6,11))
for i in range(len(list1)):
    myLink.append(list1[i])


myLink.print_list()
# print(myLink.)

