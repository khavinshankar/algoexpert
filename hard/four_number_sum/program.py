# time = O(n^3) and space = O(n^2)
def fourNumberSum(nums, target):
    pairs = {}
    quads = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            pair_sum = nums[i] + nums[j]
            diff = target - pair_sum
            if diff in pairs:
                for pair in pairs[diff]:
                    quads.append(pair + [nums[i], nums[j]])

        for j in range(i):
            pair_sum = nums[i] + nums[j]
            if pair_sum in pairs: pairs[pair_sum].append([nums[i], nums[j]])
            else: pairs[pair_sum] = [[nums[i], nums[j]]]
    
    return quads