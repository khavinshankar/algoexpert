import math

# time = O(n^2) and space = O(n^2)
def palindromePartitioningMinCuts(string):
    palindromes = [[False for char in string] for char in string]
    for i in range(len(string)):
        palindromes[i][i] = True

    for length in range(2, len(string) + 1):
        for start in range(0, len(string) + 1 - length):
            end = start + length - 1
            if length == 2: palindromes[start][end] = string[start] == string[end]
            else: palindromes[start][end] = string[start] == string[end] and palindromes[start+1][end-1]

    cuts = [math.inf for char in string]
    for end in range(len(string)):
        if palindromes[0][end]: cuts[end] = 0
        else:
            cuts[end] = cuts[end-1] + 1
            for start in range(end):
                if palindromes[start][end]: cuts[end] = min(cuts[start-1] + 1, cuts[end])

    return cuts[-1]