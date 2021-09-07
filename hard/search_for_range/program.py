# time = O(logn) and space = O(1)
def searchForRange(array, target):
    return [binarySearch(array, target, True), binarySearch(array, target, False)]

def binarySearch(array, target, getLower):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            if getLower:
                if mid == 0 or array[mid - 1] != target: return mid
                else: right = mid - 1 
            else:
                if mid == len(array) - 1 or array[mid + 1] != target: return mid
                else: left = mid + 1 
        elif array[mid] > target: right = mid - 1
        else: left = mid + 1

    return -1