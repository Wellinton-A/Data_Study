
class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        if type(key) == str:
            hash_n = ord(key[len(key) % 2]) % self.size
        if type(key) == int:
            hash_n = ord(key[len(key) % 2]) % self.size
            
        if type(key) == float:
            print(10.5)
    
    

hash1 = HashTable(20)

hash1.hash_function()