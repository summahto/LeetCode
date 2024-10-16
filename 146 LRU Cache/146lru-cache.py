class ListNode:
    def __init__(self, key= -1, value= -1):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.addToHead(node)
            return self.dic[key].value
        
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.addToHead(node)
            node.value = value

        else :
            if len(self.dic) >= self.capacity:    
                self.removeFromTail()
                
            node = ListNode(key, value)
            self.dic[key] = node
            self.addToHead(node)
    
    def addToHead(self, curr) -> None:
        headNext = self.head.next
        self.head.next = curr
        curr.next = headNext
        curr.prev = headNext.prev
        headNext.prev = curr



    def removeFromList(self, curr) -> None:
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
    
    def removeFromTail(self) -> None:
        if len(self.dic) == 0:
            return 
        tailNode = self.tail.prev
        del self.dic[tailNode.key]
        self.removeFromList(tailNode)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)