# time = O(n) and space = O(n)
def longestSubstringWithoutDuplication(string):
    rec = {}
    substr = [0, 1]
    start = 0
    for i in range(len(string)):
        if string[i] in rec:
            start = max(rec[string[i]] + 1, start)
        if substr[1] - substr[0] < i+1 - start:
            substr = [start, i+1]
        rec[string[i]] = i
    
    return string[substr[0] : substr[1]]