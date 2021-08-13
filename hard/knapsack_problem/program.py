# time = O(nc) and space = O(nc) => n = len(items) | c = capacity
def knapsackProblem(items, capacity):
    dp = [[0 for j in range(capacity + 1)] for i in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        value = items[i-1][0]
        weight = items[i-1][1]
        for cap in range(1 , capacity + 1):
            if cap >= weight: dp[i][cap] = max(dp[i-1][cap], dp[i-1][cap - weight] + value)
            else: dp[i][cap] = dp[i-1][cap]

        selected = []
        i = len(dp) - 1
        j = len(dp[0]) - 1
        while i > 0:
            if j == 0: break
            if dp[i][j] != dp[i-1][j]:
                selected.append(i-1)
                j -= items[i-1][1] 
            i -= 1

    return [dp[-1][-1], list(reversed(selected))]