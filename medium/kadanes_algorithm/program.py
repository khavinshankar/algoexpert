import math

# time = O(n) and space = O(1)
def kadanesAlgorithm(nums):
    max_sum = -math.inf
    curr_sum = -math.inf

    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    
    return max_sum