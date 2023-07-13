# two window method

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = prices[0]
        max_val = prices[0]
        for p in prices:
            if p > max_val:
                max_val = p

            if p < min_val:
                # start a new window
                max_profit = max(max_profit, max_val - min_val)
                min_val = p
                # As we cannot go back, need to reinitialize window, so max is reset: once we go overbound
                max_val = -1 
        #    print(f'max_val is {max_val}')
        #    print(f'min_val is {min_val}')
        #    print(f'profit is {p_max}')
        
        return max(max_profit, max_val - min_val)
    
# Two pointer method

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell = 1
        max_profit = 0 
        while sell < len(prices):
            cur_profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(cur_profit, max_profit)
            else:
                buy = sell
            sell += 1
        return max_profit 