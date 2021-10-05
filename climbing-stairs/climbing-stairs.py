# DP array stores previous values (number of ways to climb stairs of height n where n is the index)

class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [0 for _ in range(n+1)]
        try:
            DP[0] = 0
            DP[1] = 1
            DP[2] = 2
        except (IndexError):
            return DP[n]
        # fibonacci numbers, DP[3] = 2+1, DP[4] = 3+2, DP[5] = 5+3 ...
        for i in range(3, n+1):
            DP[i] = DP[i-1] + DP[i-2]
        return DP[n]