class ContinuousMedianHandler:
    def __init__(self):
        self.left = Heap(MAX_HEAP_COMP, [])
        self.right = Heap(MIN_HEAP_COMP, [])
        self.median = None

    # time = O(logn) and space = O(n)
    def insert(self, number):
        if not self.left.length or self.left.peek() > number:
            self.left.insert(number)
        else:
            self.right.insert(number)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        if self.left.length - self.right.length == 2:
            self.right.insert(self.left.remove())
        elif self.right.length - self.left.length == 2:
            self.left.insert(self.right.remove())

    def updateMedian(self):
        if self.left.length == self.right.length:
            self.median = (self.left.peek() + self.right.peek()) / 2;
        elif self.left.length > self.right.length:
            self.median = self.left.peek();
        else:
            self.median = self.right.peek();

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, compare, array):
        self.heap = array
        self.compare = compare
        self.length = len(self.heap)
        self.buildHeap()

    def buildHeap(self):
        heap = self.heap
        last_parent = (len(heap) - 2) // 2
        for i in reversed(range(last_parent + 1)):
            self.siftDown(i)

    def siftDown(self, i):
        heap = self.heap
        child1 = 2*i + 1
        while child1 < len(heap):
            child2 = 2*i + 2
            if child2 < len(heap):
                j = child1 if self.compare(heap[child1], heap[child2]) else child2
            else:
                j = child1
            
            if self.compare(heap[j], heap[i]):
                self.swap(i, j)
                i = j
                child1 = 2*i + 1
            else: break

    def siftUp(self, i):
        heap = self.heap
        parent = (i - 1) // 2
        while i > 0 and self.compare(heap[i], heap[parent]):
            self.swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        heap = self.heap
        heap.append(value)
        self.siftUp(len(heap) - 1)
        self.length += 1

    def remove(self):
        heap = self.heap
        self.swap(0, len(heap) - 1)
        value = heap.pop()
        self.siftDown(0)
        self.length -= 1
        return value

    def swap(self, i, j):
        heap = self.heap
        heap[i], heap[j] = heap[j], heap[i]


def MAX_HEAP_COMP(a, b):
    return a > b


def MIN_HEAP_COMP(a, b):
    return a < b