class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left

    def remove(self, node):
        nxt, prev = node.nxt, node.prev
        prev.nxt, nxt.prev = nxt, prev

    def insert(self, node):
        nxt, prev = self.right, self.right.prev
        node.nxt, node.prev = nxt, prev
        nxt.prev = prev.nxt = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key] 
        
