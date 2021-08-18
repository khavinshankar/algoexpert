class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size or 1
        self.size = 0
        self.dlist = DoublyLinkedList()
        self.cache = {}

    # time = O(1) and space = O(1)
    def insertKeyValuePair(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.dlist.setAsHead(node)
            return
        
        if self.size == self.max_size:
            self.cache.pop(self.dlist.tail.key)
            self.dlist.removeTail()
            self.size -= 1
        
        self.size += 1
        node = Node(key, value)
        self.cache[key] = node
        self.dlist.insertAsHead(node)

    # time = O(1) and space = O(1)
    def getValueFromKey(self, key):
        if key in self.cache: 
            self.dlist.setAsHead(self.cache[key])
            return self.cache[key].value
        return None

    # time = O(1) and space = O(1)
    def getMostRecentKey(self):
        return self.dlist.head.key

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAsHead(self, node):
        if self.head == None: self.head = self.tail = node

        self.head.prev = node
        node.next = self.head
        self.head = node


    def setAsHead(self, node):
        if node == self.head: return
        
        is_tail = False
        if node == self.tail: is_tail = True

        prev_ = node.prev
        next_ = node.next

        prev_.next = next_
        if not is_tail: next_.prev = prev_
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        if is_tail: self.tail = prev_


    def removeTail(self):
        if self.tail == self.head: 
            self.head = self.tail = None
            return
        prev_ = self.tail.prev
        
        prev_.next = None
        self.tail = prev_
    
    def printList(self):
        curr = self.head
        while curr != self.tail:
            print(f"({curr.key}, {curr.value}) <-> ", end="")
            curr = curr.next
        print(f"({self.tail.key}, {self.tail.value})")