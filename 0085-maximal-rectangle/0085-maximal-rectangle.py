class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if not rows: return 0
        
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            size = 0
            for c in range(cols):
                if matrix[r][c] == "1":
                    size += 1
                else:
                    size = 0
                dp[r][c] = size
        
        res = 0
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                width = dp[r][c]
                height = 0
                k = r
                
                while k > -1 and dp[k][c]:
                    height += 1
                    width = min(width, dp[k][c])
                    res = max(res, width * height)
                    k -= 1
        return res