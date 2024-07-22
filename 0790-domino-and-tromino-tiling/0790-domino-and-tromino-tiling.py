class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][0] represents tiling until i-th column with 0 gaps
        # dp[i][1] represents tiling until i-th column leaving 1 square
        
        dp = [[0, 0] for _ in range(n+2)]
        dp[1], dp[2] = [1, 1], [2, 1]
        
        for i in range(3, n+1):
            # tile until prev column (i-1) + 1  = 1 way
            # tile until prevprev column (i-2) + 1 (2 horizontal) = 1 way
            # tile until prev column with a gap but with 2 orientation (2 way)
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2*dp[i-1][1]
            
            # tile until prevprev + 1 tromino = 1 way
            # tile until prev with a gap + 1 domino = 1 way
            dp[i][1] = dp[i-2][0] + dp[i-1][1]
        return dp[n][0] % MOD
