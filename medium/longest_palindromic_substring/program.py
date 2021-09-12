# time = O(n^2) and space = O(1)
def longestPalindromicSubstring(string):
    substring = 0, 0
    for i in range(1, len(string)):
        odd = longestPalindromeFrom(i-1, i+1, string)
        even = longestPalindromeFrom(i-1, i, string)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        substring = max(substring, longest, key=lambda x: x[1] - x[0])

    return string[substring[0]: substring[1]+1]

def longestPalindromeFrom(left, right, string):
    while left >= 0 and right < len(string):
        if string[left] != string[right]: break
        left -= 1; right += 1

    return left+1, right-1