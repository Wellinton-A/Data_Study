class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return 
        currentNode = self.root
        while True:
            if value < currentNode.value:
                if currentNode.left == None:
                    currentNode.left = new_node
                    return
                else:
                    currentNode = currentNode.left
            elif currentNode.right == None:
                currentNode.right = new_node
                return
            else:
                currentNode = currentNode.right
        return
        
    def lookup(self, value):
        currentNode = self.root
        while currentNode != None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return currentNode.value, True

def print_tree(root):
    if root:
        print(root.value)
        print_tree(root.left)
        print_tree(root.right)

myBinaryST = BinarySearchTree()
myBinaryST.insert(105)
myBinaryST.insert(50)
myBinaryST.insert(75)
myBinaryST.insert(150)
myBinaryST.insert(125)
myBinaryST.insert(155)
myBinaryST.insert(45)
myBinaryST.insert(2)
print_tree(myBinaryST.root)
print(myBinaryST.lookup(45))


