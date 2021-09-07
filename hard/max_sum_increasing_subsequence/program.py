# time = O(n^2) and space = O(n)
def maxSumIncreasingSubsequence(array):
    sums = [array[0]]
    idxs = [None]
    max_sum_idx = 0
    for i in range(1, len(array)):
        curr = array[i]
        sums.append(curr)
        idxs.append(None)
        for j in range(0, i):
            if curr > array[j]:
                if sums[i] <= curr + sums[j]:
                    sums[i] = curr + sums[j]
                    idxs[i] = j
        if sums[i] > sums[max_sum_idx]: max_sum_idx = i
    
    return [sums[max_sum_idx], getSubsequence(array, idxs, max_sum_idx)]

def getSubsequence(array, idxs, max_sum_idx):
    curr = max_sum_idx
    sequence = []
    while curr is not None:
        sequence.append(array[curr])
        curr = idxs[curr]
    
    return list(reversed(sequence))