import math

# time = O(n^2) and space = O(d) => n = len(arr1 or arr2) | d = depth of the bst
def sameBsts(arr1, arr2, i1=0, i2=0, low=-math.inf, high=math.inf):
    if i1 == -1 or i2 == -1: return i1 == i2
    if arr1[i1] != arr2 [i2]: return False

    left1 = getLeft(arr1, i1, low, high)
    left2 = getLeft(arr2, i2, low, high)
    left = sameBsts(arr1, arr2, left1, left2, low, arr1[i1])

    right1 = getRight(arr1, i1, low, high)
    right2 = getRight(arr2, i2, low, high)
    right = sameBsts(arr1, arr2, right1, right2, arr1[i1], high)
    
    return left and right

def getLeft(arr, i, low, high):
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[i] and arr[j] >= low and arr[j] < high: return j
    return -1

def getRight(arr, i, low, high):
    for j in range(i + 1, len(arr)):
        if arr[j] >= arr[i] and arr[j] >= low and arr[j] < high: return j
    return -1