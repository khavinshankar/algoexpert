class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.buildHeap()

    # time = O(n) and space = O(1)
    def buildHeap(self):
        heap = self.heap
        last_parent = (len(heap) - 2) // 2
        for i in reversed(range(last_parent + 1)):
            self.siftDown(i)

    # time = O(logn) and space = O(1)
    def siftDown(self, i):
        heap = self.heap
        child1 = 2*i + 1
        while child1 < len(heap):
            child2 = 2*i + 2
            if child2 < len(heap):
                j = child1 if heap[child1] < heap[child2] else child2
            else:
                j = child1
            
            if heap[j] < heap[i]:
                self.swap(i, j)
                i = j
                child1 = 2*i + 1
            else: break

    # time = O(logn) and space = O(1)
    def siftUp(self, i):
        heap = self.heap
        parent = (i - 1) // 2
        while i > 0 and heap[i] < heap[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    # time = O(1) and space = O(1)
    def peek(self):
        return self.heap[0]

    # time = O(logn) and space = O(1)
    def insert(self, value):
        heap = self.heap
        heap.append(value)
        self.siftUp(len(heap) - 1)

    # time = O(logn) and space = O(1)
    def remove(self):
        heap = self.heap
        self.swap(0, len(heap) - 1)
        value = heap.pop()
        self.siftDown(0)
        return value

    def swap(self, i, j):
        heap = self.heap
        heap[i], heap[j] = heap[j], heap[i]
