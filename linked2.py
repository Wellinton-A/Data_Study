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

    def transverse(self, index):
        i=0
        current_node = self.head
        while i < index:
            current_node = current_node.next
            i+=1
        return current_node

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        if index >= self.length:
            self.append(value)
            return
        leader = self.transverse(index-1)
        pointer = self.transverse(index)
        new_node = Node(value)
        leader.next = new_node
        new_node.next = pointer
        self.length +=1
    
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        leader = self.transverse(index-1)
        pointer = self.transverse(index+1)
        leader.next = pointer
        self.length -=1

    def print_list(self):
        list_linked = []
        current_node = self.head
        while current_node != None:
            list_linked.append(current_node.value)
            current_node = current_node.next
        return print(list_linked)
myLink = LinkedList(10)
myLink.append(25)
myLink.append(52)
myLink.prepend(15)
myLink.prepend(14)
myLink.prepend(13)

print(myLink.transverse(0).next.value)
myLink.print_list()
# print(myLink.length)
# myLink.print_tail()