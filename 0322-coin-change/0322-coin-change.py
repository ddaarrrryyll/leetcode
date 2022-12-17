class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        # initialise 2d dp matrix
        dp = [[inf] * (amount + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 0
            for amt in range(1, amount+1):
                # dont take coin
                dp[i][amt] = dp[i-1][amt]
                
                # if current amount more than current coin, check the min number of coins with above (dont take) and below (take)
                if amt >= coins[i]:
                    dp[i][amt] = min(dp[i][amt], dp[i][amt-coins[i]] + 1)
                    
        return dp[n-1][amount] if dp[n-1][amount] != inf else -1