# time = O(n^2) and space = O(n)
def numberOfBinaryTreeTopologies(n, memo={}):
    if n in memo: return memo[n]
    if n == 0: return 1

    topologies = 0
    for i in range(n):
        left = numberOfBinaryTreeTopologies(n-1-i, memo)
        right = numberOfBinaryTreeTopologies(i, memo)
        topologies += (left * right)
    
    memo[n] = topologies
    return topologies

# time = O(n^2) and space = O(n)
def numberOfBinaryTreeTopologiesIter(n):
    memo = [1]
    for i in range(1, n+1):
        topologies = 0
        for j in range(i):
            left = memo[i-1-j]
            right = memo[j]
            topologies += (left * right)
        
        memo.append(topologies)
    
    return memo[n]  