class HashTable:
    def __init__(self, size):  # Constructor method, initializes the hash table with a given size
        self.size = size  # Store the size of the hash table
        self.table = [[] for _ in range(size)]  # Create a list of empty lists, one for each slot in the hash table

    def _hash(self, key):  # Helper method to compute the hash value of a key
        return hash(key) % self.size  # Compute the hash value and use modulo to ensure it falls within the table size

    def insert(self, key, value):  # Method to insert a key-value pair into the hash table
        index = self._hash(key)  # Get the index where the key-value pair will be stored
        for pair in self.table[index]:  # Iterate through the key-value pairs stored at that index
            if pair[0] == key:  # If the key already exists, update its value
                pair[1] = value
                return
        self.table[index].append([key, value])  # If the key doesn't exist, append a new key-value pair to the list

    def get(self, key):  # Method to retrieve the value associated with a given key
        index = self._hash(key)  # Get the index where the key-value pair is stored
        for pair in self.table[index]:  # Iterate through the key-value pairs stored at that index
            if pair[0] == key:  # If the key is found, return its value
                return pair[1]
        raise KeyError(key)  # If the key is not found, raise a KeyError

    def remove(self, key):  # Method to remove a key-value pair from the hash table
        index = self._hash(key)  # Get the index where the key-value pair is stored
        for i, pair in enumerate(self.table[index]):  # Iterate through the key-value pairs stored at that index
            if pair[0] == key:  # If the key is found, remove the key-value pair
                del self.table[index][i]
                return
        raise KeyError(key)  # If the key is not found, raise a KeyError
