class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = prices[-1]
        max_profit = 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            max_profit = max(max_profit, max_price - prices[i])
        return max_profit