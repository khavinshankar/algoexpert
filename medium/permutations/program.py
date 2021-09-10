# time = O(n*n!) and space = O(n*n!)
def permutations(nums):
    perms = []
    getPermutations(nums, 0, perms)
    return perms

def getPermutations(nums, i, perms):
    if i == len(nums) - 1: perms.append([*nums])

    for j in range(i, len(nums)):
        swap(nums, i, j)
        getPermutations(nums, i+1, perms)
        swap(nums, i, j)
    

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]