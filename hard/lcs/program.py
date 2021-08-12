# time = O(nm) and space = O(nm)
def longestCommonSubsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    lcs = [[[None, 0] for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str2[i-1] == str1[j-1]:
                lcs[i][j] = [str2[i-1], lcs[i-1][j-1][1] + 1]
            else:
                lcs[i][j] = [None, max(lcs[i-1][j][1], lcs[i][j-1][1])]
                
    return getLCS(lcs)

def getLCS(lcs):
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    
    sequence = ""
    while not lcs[i][j][1] == 0:
        if lcs[i][j][0] == None:
            if lcs[i-1][j][1] > lcs[i][j-1][1]: i -= 1  
            else: j -= 1
        else:
            sequence += lcs[i][j][0]
            i -= 1
            j -= 1
    
    return list(reversed(sequence))




    
