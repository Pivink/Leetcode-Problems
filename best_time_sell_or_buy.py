def best_time(prices):
    buy_price=prices[0]
    profit=0
    for i in range(1,len(prices)):
        if buy_price>prices[i]:
            buy_price=prices[i]
        profit=max(profit,prices[i]-buy_price)
    return profit
print(best_time([7,1,5,3,6,4]))