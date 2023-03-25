class BloomFilter:

    def __init__(self, number_hash_functions, number_bits):
        self.number_bits = number_bits
        self.array = [0]*number_bits
        self.number_hash_functions = number_hash_functions

    def repeated_hash(self, key, repeats):
        current_hash = hash(str(key))
        for i in range(2, repeats):
            current_hash = hash(str(current_hash))
        return current_hash

    def add_key(self, key):
        hashes = [self.repeated_hash(key, i) for i in range(self.number_hash_functions)]
        indexes = [current_hash % self.number_bits for current_hash in hashes]
        for index in indexes:
            self.array[index] = 1

    def check_key(self, key):
        hashes = [self.repeated_hash(key, i) for i in range(self.number_hash_functions)]
        indexes = [current_hash % self.number_bits for current_hash in hashes]
        for index in indexes:
            if self.array[index] == 0:
                return False
        return True
    