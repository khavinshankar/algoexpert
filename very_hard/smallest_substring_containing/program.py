import math

# time = O(b+s) and space = O(s)
def smallestSubstringContaining(big_str, small_str):
    char_rec = {}
    for char in small_str:
        if char in char_rec: char_rec[char] += 1
        else: char_rec[char] = 1
    
    start = end = 0
    found = 0
    match = [math.inf, 0, 0] # length, start, end
    while end <= len(big_str):
        if found == len(small_str):
            curr_len = end - start
            if curr_len < match[0]: match = [curr_len, start, end]
            
            if big_str[start] in char_rec:
                if char_rec[big_str[start]] == 0: found -= 1
                char_rec[big_str[start]] += 1
            start += 1
        else:
            if end == len(big_str): break

            if big_str[end] in char_rec:
                if char_rec[big_str[end]] > 0: found += 1
                char_rec[big_str[end]] -= 1
            end += 1

    return big_str[match[1]: match[2]]