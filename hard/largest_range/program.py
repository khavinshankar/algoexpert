# time = O(n) and space = O(n)
def largestRange(nums):
    rec = {num: False for num in nums}
    start = -1
    end = -1

    for num in nums:
        if rec[num]: continue
        
        left = num - 1
        while left in rec:
            rec[left] = False
            left -= 1
        right = num + 1
        while right in rec:
            rec[right] = False
            right += 1

        if (end - start) <= (right - left - 2):
            start = left + 1
            end = right - 1

    return [start, end]