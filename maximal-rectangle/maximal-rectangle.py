class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        
        # empty matrix
        if not rows:
            return 0
        cols = len(matrix[0])
        
        dp = [[0] * cols for _ in range(rows)]
        
        # left to right
        for r in range(rows):
            size = 0
            for c in range(cols):
                if matrix[r][c] == "1":
                    size += 1
                else:
                    size = 0
                
                dp[r][c] = size
        
        out = 0
        # bottom to top
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                width = dp[r][c]
                height = 0 # right side
                k = r
                
                # iterate upwards if dp[k][j] is part of a rectangle, first pass will always be the size of the row-wise rectangle (single row)
                while k > -1 and dp[k][c]:
                    # enters if there is 1 in current cell / if k is not out of the matrix
                    height += 1
                    width = min(width, dp[k][c])
                    out = max(out, width * height)
                    k -= 1
                    # print(out)
        return out