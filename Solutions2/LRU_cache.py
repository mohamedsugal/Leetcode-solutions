class Node: 
    def __init__(self, key, value): 
        self.key = key
        self.value = value
        self.next = None
        self.prev = None 

class LRUCache: 
    def __init__(self, capacity):
        self.capacity = capacity 
        self.dictionary = {}
        self.head = Node(0, 'H')
        self.tail = Node(0, 'T')
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node): 
        temp = self.head.next 
        temp.prev = node 
        node.next = temp
        node.prev = self.head
        self.head.next = node 
        
    
    def _remove(self, node): 
        p = node.prev 
        n = node.next 
        p.next = n 
        n.prev = p

    
    def put(self, key, value): 
        if key in self.dictionary: 
            self._remove(self.dictionary[key])
        n = Node(key, value)
        self._add(n)
        self.dictionary[key] = n 
        if len(self.dictionary) > self.capacity: 
            n = self.tail.prev
            self._remove(n)
            del self.dictionary[n.key]
    
    def get(self, key): 
        if key in self.dictionary: 
            n = self.dictionary[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def __str__(self): 
        result = ""
        node = self.head 
        while node: 
            if node == self.tail: 
                result += str(node.value)
            else: 
                result += str(node.value) + " - "
            node = node.next 
        return result

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)

print(cache)
print(cache.get(2))