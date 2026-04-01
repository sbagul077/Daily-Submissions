class Node:

    def __init__(self, key,val):        
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    hashMap = dict()
    capacity = 0
    def __init__(self, capacity: int):
        self.hashMap = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node


    def get(self, key: int) -> int:
        if key not in self.hashMap.keys():
            return -1
        
        currNode = self.hashMap.get(key)
        self.removeNode(currNode)
        self.addNode(currNode)
        return currNode.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap.keys():
            newNode = Node(key, value)
            self.removeNode(self.hashMap.get(key))
            self.addNode(newNode)
            self.hashMap[key] = newNode
        else:
            if len(self.hashMap) == self.capacity:
                tailPrevNode = self.tail.prev
                self.removeNode(tailPrevNode)
                del self.hashMap[tailPrevNode.key]
            
            newNode = Node(key, value)
            self.addNode(newNode)
            self.hashMap[key] = newNode





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)