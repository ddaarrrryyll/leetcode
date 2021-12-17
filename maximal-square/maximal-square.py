class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        
        if not rows:
            return 0
        
        cols = len(matrix[0])
        
        dp = [[0] * cols for _ in range(rows)]
        
        out = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
                    out = max(out, dp[r][c] ** 2)
                    
        return out
                