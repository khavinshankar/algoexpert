import math

# time = O(n^3 + m) and space = O(n + m) => n = len(pi) | m = len(nums)
def numbersInPi(pi, nums):
    nums = {num: True for num in nums}
    spaces = minSpaces(pi, nums, 0, {})
    return -1 if spaces == math.inf else spaces

def minSpaces(pi, nums, i, memo):
    if i in memo: return memo[i]
    if i == len(pi): return -1 # to remove the space at the very end

    spaces = math.inf
    for j in range(i, len(pi)):
        prefix = pi[i: j+1]
        if prefix in nums:
            spaces = min(spaces, minSpaces(pi, nums, j+1, memo) + 1)
    
    memo[i] = spaces
    return spaces