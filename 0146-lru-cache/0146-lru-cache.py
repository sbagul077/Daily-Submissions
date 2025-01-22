class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = 0
        self.prev = 0

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def addNode(self, node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map.keys():
            return -1
        node = self.map.get(key)
        self.removeNode(node)
        self.addNode(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map.get(key)
            node.val = value
            self.removeNode(node)
            self.addNode(node)
        else:
            if self.capacity == len(self.map):
                tailPrev = self.tail.prev
                self.removeNode(tailPrev)
                del self.map[tailPrev.key]
            newNode = Node(key, value)
            self.addNode(newNode)
            self.map[key] = newNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)