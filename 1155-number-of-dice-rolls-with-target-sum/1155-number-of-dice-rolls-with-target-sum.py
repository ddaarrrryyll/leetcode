class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0 for _ in range(target+1)]
        for i in range(1, min(k, target) + 1):
            dp[i] = 1
        
        for i in range(n-1):
            for j in range(target, 0, -1):
                count = 0
                for m in range(1, k+1):
                    if j - m >= 1:
                        count += dp[j-m]
                dp[j] = count
                
        return dp[-1] % (10**9 + 7)