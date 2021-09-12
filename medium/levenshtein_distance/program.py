# time = O(sb) and space = O(s)
def levenshteinDistance(str1, str2):
    small_str, big_str = (str1, str2) if len(str1) < len(str2) else (str2, str1)
    s, b = len(small_str), len(big_str) 
    odd = [i for i in range(s+1)]
    even = [0 for i in range(s+1)]

    for i in range(1, b+1):
        if i % 2 == 0: 
            curr = even
            prev = odd
        else:
            curr = odd
            prev = even
        
        curr[0] = i
        for j in range(1, s+1):
            if small_str[j-1] == big_str[i-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(curr[j-1], prev[j], prev[j-1])
        
    return even[-1] if b % 2 == 0 else odd[-1]