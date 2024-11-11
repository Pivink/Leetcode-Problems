def best_time(prices):
    profit=0
    start=prices[0]
    for i in range(1,len(prices)):
        if start<prices[i]:
            profit+=prices[i]-start
        start=prices[i]
    return profit
print(best_time([1,2,3,4,5]))