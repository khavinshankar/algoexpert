# time = O(nlogn) and space = O(1)
def heapSort(array):
    buildMaxHeap(array)
    for i in reversed(range(1, len(array))):
        swap(0, i, array)
        siftDown(0, i-1, array)
    
    return array

def buildMaxHeap(array):
    last_parent = (len(array) - 2) // 2
    for i in reversed(range(last_parent + 1)):
        siftDown(i, len(array) - 1, array)

def siftDown(curr, end, heap):
    child1 = curr * 2 + 1
    while child1 <= end:
        child2 = curr * 2 + 2
        swap_i = None
        if child2 <= end and heap[child1] < heap[child2]:
            swap_i = child2
        else:
            swap_i = child1
        
        if heap[swap_i] > heap[curr]:
            swap(swap_i, curr, heap)
            curr = swap_i
            child1 = curr * 2 + 1
        else: break

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]