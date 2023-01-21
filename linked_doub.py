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

    def transverse(self, index):
        i=0
        current_node = self.head
        while i < index:
            current_node = current_node.next
            i += 1
        return current_node

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        if index >= self.length:
            self.append(value)
            return
        new_node = Node(value)
        leader = self.transverse(index-1)
        follower = self.transverse(index)
        leader.next = new_node
        new_node.previous = leader
        new_node.next = follower
        follower.previous = new_node
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
            return
        if index > self.length:
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1
            return
        leader = self.transverse(index-1)
        follower = self.transverse(index+1)
        leader.next = follower
        follower.previous = leader
        self.length -= 1
        

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
myLink.insert(8, 3)

list1 = list(range(6,11))
for i in range(len(list1)):
    myLink.append(list1[i])
myLink.remove(3)

print(myLink.tail.value)
myLink.print_list()
# print(myLink.)

