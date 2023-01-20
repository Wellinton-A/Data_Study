class Node:
    def __init__(self, value):
        self.value: None
        self.next: None

class LinkedList:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        newNode = {
            "value": value,
            "next": None
        }
        self.tail.update({"next": newNode})
        self.tail = newNode
        self.length += 1
    
    def prepend(self, value):
        newNode = {
            "value": value,
            "next": self.head
        }
        self.head = newNode
        self.length += 1
    
    # def __repr__(self):
    #     return f"head = {self.head}\ntail = {self.tail}\nlength = {self.length}"


Mylink = LinkedList(10)
# print(Mylink)
Mylink.append(11)
print(Mylink)
Mylink.prepend(25)
print(Mylink)
Mylink.prepend(52)
print(Mylink)

list1 =list(range(1000))

for i in list1:
    Mylink.append(i)

print(Mylink)

for i in list1:
    Mylink.prepend(i)
print(Mylink)