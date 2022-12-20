class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # because you will either land on cost[-2] or cost[-1], we can start from there
        
        dp = [-1 for _ in range(len(cost))]
        dp[-1], dp[-2] = cost[-1], cost[-2]
        for i in range(len(cost)-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        # print(dp)
        return min(dp[0], dp[1])