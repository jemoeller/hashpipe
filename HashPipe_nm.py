#import sys

class HashPipe(object):

    def __init__(self):
        self.size = 32# hvorfor?
        self.map = [None] * self.size#creating the initial pipe

    def get_hash(self, key):#returns the hash for a given key
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash

    def get_height(self, key):#returns the height of the pipe in which the key resides.
        binary = format(ord(key), 'b')
        counter = 0
        for i in range(len(binary)-1,-1,-1):
            if binary[i] == '1':
                counter += 1
                return counter
            else:
                counter += 1

    def get_size(self):#just returns 5001 or 32 in this case
        return self.size

    def put(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key, value])
            return True
        else:
            if self.map[key_hash][0] == key:
                self.map[key_hash][1] = value
                return True

    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
                if self.map[key_hash][0] == key:
                    return self.map[key_hash][1]
        return None

    def floor(self, key):
        key_hash = self.get_hash(key)
        key_hash -= 1
        while key_hash < len(self.map):
            if self.map[key_hash] is not 0:
                return self.map[key_hash][0]
            key_hash -= 1
        return None

    """For ease of use I implemented a next function
       that I used in the control function.
       However, I made the floor function anyway."""
    def next(self, key):
        key_hash = self.get_hash(key)
        key_hash += 1
        while key_hash < len(self.map):
            if self.map[key_hash] is not None:
                return self.map[key_hash][0]
            key_hash += 1
        return None

    def control(self, key, height):
        height += 1
        next_key = self.next(key)
        if next_key is None:
            return "."
        else:
            next_height = self.get_height(next_key)
            while True:
                if height > self.get_height(key):
                    return "."
                if next_height >= height:
                    return next_key
                if next_height < height:
                    next_key = self.next(next_key)
                    if next_key is None:
                        return "."
                    next_height = self.get_height(next_key)

if __name__ == "__main__":
    print(hash("i"))
    