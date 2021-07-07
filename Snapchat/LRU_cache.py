class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.prev = None 
        self.next = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail 
        self.tail.prev = self.head 

    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity: 
            temp = self.tail.prev 
            self.remove(temp)
            del self.cache[temp.key]
        
    def add(self, node): 
        temp = self.head.next 
        temp.prev = node 
        node.next = temp 
        node.prev = self.head
        self.head.next = node 
    
    def remove(self, node): 
        p = node.prev 
        n = node.next 
        p.next = n 
        n.prev = p 


lru_cache = LRUCache(2)
print("Capacity [2]")
print("Put (1,1)", end="")
lru_cache.put(1, 1)
print()
print("Put (2,2)", end="")
lru_cache.put(2, 2)
print()
print("Get (1): ", lru_cache.get(1))
print("Put (3,3)", end="")
lru_cache.put(3, 3)
print()
print("Get (2): ", lru_cache.get(2))
print("Put (4,4)", end="")
lru_cache.put(4, 4)
print()
print("Get (1): ", lru_cache.get(1))
print("Get (3): ", lru_cache.get(3))
print("Get (4): ", lru_cache.get(4))

