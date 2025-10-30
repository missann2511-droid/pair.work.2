def cut_rod(prices, n):
    """
    Finds the list of cuts for the rod of length n to maximize profit.
    Args:
        prices (list): prices[i] -- price for a piece of length (i+1)
        n (int): length of the rod
    Returns:
        tuple: (max_profit, cuts_list)
    """
    dp = [0] * (n + 1)
    cuts = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            if max_val < prices[j - 1] + dp[i - j]:
                max_val = prices[j - 1] + dp[i - j]
                cuts[i] = j
        dp[i] = max_val
        
    res = []
    length = n
    while length > 0:
        res.append(cuts[length])
        length -= cuts[length]

    return dp[n], res

prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
max_profit, cuts_list = cut_rod(prices, n)
print("Maximum obtainable value:", max_profit)
print("Recommended cuts (lengths):", cuts_list)
