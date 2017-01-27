def maxProfit( prices):
    profit = 0
    for i in range(1,len(prices)):
        pt = prices[i]-prices[i-1]
        if pt>0: profit += pt
    return pt

print maxProfit([2,3,1,5])
