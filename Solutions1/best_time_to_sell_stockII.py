def sell_stock_II(prices): 
    max_profit = 0
    for i in range(len(prices)-1): 
        if prices[i] < prices[i+1]: 
            max_profit += prices[i+1] - prices[i]
    return max_profit

prices = [7,1,5,3,6,4]
print(sell_stock_II(prices))
