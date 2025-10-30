def cut_rod(prices, n):
    dp = [0] * (n + 1)
    cuts = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, i + 1):
            if j - 1 < len(prices):
                current = prices[j - 1] + dp[i - j]
                if current > max_val:
                    max_val = current
                    cuts[i] = j
        dp[i] = max_val
        
    result = []
    remaining = n
    while remaining > 0:
        result.append(cuts[remaining])
        remaining -= cuts[remaining]

    return result

prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
cuts_list = cut_rod(prices, n)
print("Recommended cuts:", cuts_list)

total_value = 0
for cut in cuts_list:
    total_value += prices[cut - 1]
print("Total value:", total_value)
