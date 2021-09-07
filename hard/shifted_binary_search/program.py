def shiftedBinarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target: return mid
        elif array[mid] >= array[left]:
            if target < array[mid] and target >= array[left]: right = mid - 1
            else: left = mid + 1
        else:
            if target > array[mid] and target <= array[right]: left = mid + 1
            else: right = mid - 1

    return -1

print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33))