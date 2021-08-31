import math

# time = O(nk) and space = O(n)
def maxProfitWithKTransactions(prices, k):
    if len(prices) == 0: return 0
    
    even_profits = [0 for _ in prices]
    odd_profits = [0 for _ in prices]
    for t in range(1, k+1):
        curr = odd_profits if t%2 else even_profits
        prev = even_profits if t%2 else odd_profits
        max_thus_far = -math.inf
        for d in range(1, len(prices)):
            max_thus_far = max(max_thus_far, prev[d-1] - prices[d-1])
            curr[d] = max(max_thus_far + prices[d], curr[d-1])
    
    return odd_profits[-1] if t%2 else even_profits[-1]