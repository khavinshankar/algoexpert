import math

# time = O(n) and space = O(1)
def subarraySort(array):
    unsorted_max = -math.inf
    unsorted_min = math.inf

    for i in range(len(array)):
        if i == 0:
            if array[i] > array[i+1]:
                unsorted_max = max(unsorted_max, array[i])
                unsorted_min = min(unsorted_min, array[i])
            continue
        if i == len(array) - 1:
            if array[i-1] > array[i]:
                unsorted_max = max(unsorted_max, array[i])
                unsorted_min = min(unsorted_min, array[i])
            continue
        if array[i] > array[i+1] or array[i] < array[i-1]:
            unsorted_max = max(unsorted_max, array[i])
            unsorted_min = min(unsorted_min, array[i])
        
    start = -1
    for i in range(len(array)):
        if array[i] > unsorted_min:
            start = i
            break

    end = -1
    for i in reversed(range(len(array))):
        if array[i] < unsorted_max:
            end = i
            break
    
    return [start, end]