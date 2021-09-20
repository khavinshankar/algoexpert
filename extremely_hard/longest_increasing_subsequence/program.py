# time = O(nlogn) and space = O(n)
def longestIncreasingSubsequence(array):
    length = 0
    smallest_indices = [None for x in array] + [None]
    sequences = [None for x in array]

    for i in range(len(array)):
        j = binarySearch(1, length, array, smallest_indices, array[i])
        sequences[i] = smallest_indices[j-1]
        smallest_indices[j] = i
        length = max(length, j)
    
    return getSequences(array, sequences, smallest_indices[length])

def binarySearch(start, end, array, smallest_indices, target):
    if start > end: return start

    mid = (start + end) // 2
    if target > array[smallest_indices[mid]]:
        start = mid + 1
    else:
        end = mid - 1
    
    return binarySearch(start, end, array, smallest_indices, target)

def getSequences(array, sequences, curr):
    sequence = []

    while curr is not None:
        sequence.append(array[curr])
        curr = sequences[curr]
    
    return list(reversed(sequence))