
# basic implementation for HashMaps

class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash_function(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(key)

    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return '{' + ', '.join(f'{k}: {v}' for k, v in items) + '}'


# Example usage:
hash_map = HashMap()
hash_map.put('a', 1)
hash_map.put('b', 2)
hash_map.put('c', 3)
print(hash_map)  # Output: {'a': 1, 'b': 2, 'c': 3}
print(hash_map.get('b'))  # Output: 2
hash_map.remove('a')
print(hash_map)  # Output: {'b': 2, 'c': 3}
