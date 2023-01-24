
class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) % ord(key[2])) * i % self.size
        return hash
    
    def add(self, key, value):
        address = self.hash_function(key)
        if self.keys[address] == None:
            self.keys[address] = key
            self.values[address] = value

    def get(self, key):
        address = self.hash_function(key)
        return self.values[address] 
    

hash1 = HashTable(85)

hash1.add('First', 1)
hash1.add('Second', 2)
hash1.add('Third', 3)
hash1.add('Forth', 4)

print(hash1.get('Forth'))


