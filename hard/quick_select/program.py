# time = O(n^2) and space = O(1)
def quickselect(array, k):
    if len(array) == 1 and k == 1: return array[0]
    
    pos = k-1
    start = 0
    end = len(array) - 1
    while True:
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(left, right, array)
            if array[left] <= array[pivot]: left += 1
            if array[right] >= array[pivot]: right -= 1
        swap(right, pivot, array)

        if right == pos: return array[pos]
        elif right >= pos: right = right - 1
        else: start = right + 1

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(quickselect([1], 1))