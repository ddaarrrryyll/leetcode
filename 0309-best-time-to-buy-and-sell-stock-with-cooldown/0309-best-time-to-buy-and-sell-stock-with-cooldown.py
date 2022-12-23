class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        b = [0] * n
        s = [0] * n
        b[0] = -prices[0]
        for i in range(1, len(prices)):
            # buy yesterday vs buy this day
            b[i] = max(b[i-1], s[i-2] - prices[i])
            # sell yesterday vs sell today
            s[i] = max(s[i-1], b[i-1] + prices[i])
        return s[-1]