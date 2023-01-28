
class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        hash = 0
        if type(key) == int:
            hash = (key**5) % self.size
            return hash
        else:
            for i in range(len(key)):
                hash = (hash + ord(key[i]) % ord(key[2])) * i % self.size
            return hash
    
    def add(self, key, value):
        address = self.hash_function(key)
        if not self.keys[address]:
            self.keys[address] = key
            self.values[address] = value
        elif type(self.keys[address]) != type([]):
            self.keys[address] = [self.keys[address]]
            self.keys[address].append(key)
            self.values[address] = [self.values[address]]
            self.values[address].append(value)
        else:
            self.keys[address].append(key)
            self.values[address].append(value)

    def get(self, key):
        address = self.hash_function(key)
        if type(self.keys[address]) != type([]): 
            return self.values[address]
        else:
            for i in range(len(self.keys[address])):
                if self.keys[address][i] == key:
                    return self.values[address][i]
         
    

hash1 = HashTable(10)

hash1.add('First', 1)
hash1.add('Second', 2)
hash1.add('Third', 3)
hash1.add('Forth', 4)
hash1.add('Fifth', 5)
hash1.add('Sixth', 6)
hash1.add('seventh', 7)
hash1.add('Eighth', 8)
hash1.add('Nineth', 9)
hash1.add('Tenth', 10)
hash1.add('Eleventh', 11)
hash1.add(1, True)
hash1.add(8, True)
hash1.add(20, True)

print(hash1.keys)
print(hash1.values)
print(hash1.get(8))



