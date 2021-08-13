# time = O(n) and space = O(n)
def minRewards(marks):
    rewards = [1 for mark in marks]
    for i in range(1, len(marks)): # 1 to n
        if marks[i] > marks[i-1]: rewards[i] = max(rewards[i], rewards[i-1] + 1)
    for i in range(len(marks)-2, -1, -1): # n-1 to 0
        if marks[i] > marks[i+1]: rewards[i] = max(rewards[i], rewards[i+1] + 1)

    return sum(rewards)